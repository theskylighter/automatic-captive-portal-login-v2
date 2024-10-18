import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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