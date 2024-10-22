import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import subprocess

def is_network_down():
                    # Try pinging a reliable server (like Google DNS)
    try:
                    # Use subprocess to ping Google DNS
        result = subprocess.run(["ping", "-n", "1", "8.8.8.8"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            return True 
                            # Network is down
        else:
            return False    # Network is up
    except Exception as e:
        print(f"Error checking network: {e}")
        return True  # Assume network is down if there's an error
    
    
def login_to_network():
    with webdriver.Edge() as driver:
        try:
            driver.get("http://172.16.1.3:8002/index.php?zone=lan&redirurl=http%3A%2F%2Fedge-http.microsoft.com%2Fcaptiveportal%2Fgenerate_204")
        except Exception as e:
            print(f"Failed to load page: {e}")
            sys.exit(1)

        try:
            username = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "auth_user"))
            )
            username.clear()

            password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "auth_pass"))
            )
            password.clear()

            username.send_keys("id")
            password.send_keys("password")

            driver.find_element(By.NAME, "accept").click()

            print("Logged In.")
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)

def main():
    print("Starting network monitoring...")
    while True:
        if is_network_down():
            print("Network down, attempting to log in...")
            login_to_network()
            break  # Exit the loop once logged in
        else:
            print("Network still up, checking again in 1 seconds...")
        time.sleep(1)  # Wait for 1 seconds before checking again

if __name__ == "__main__":
    main()