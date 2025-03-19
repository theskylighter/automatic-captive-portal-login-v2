import requests
import time
import subprocess
import sys

# Replace with your actual credentials
USERNAME = "2023uai1819"
PASSWORD = "0000000000"

# Captive portal login URL
LOGIN_URL = "http://172.16.1.3:8002/index.php?zone=lan"

# Headers (captured from your request)
HEADERS = {
    "Host": "172.16.1.3:8002",
    "Cache-Control": "max-age=0",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "http://172.16.1.3:8002",
    "Content-Type": "application/x-www-form-urlencoded",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "http://172.16.1.3:8002/index.php?zone=lan&redirurl=http%3A%2F%2Fedge-http.microsoft.com%2Fcaptiveportal%2Fgenerate_204",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

# Form data (captured from your request)
PAYLOAD = {
    "redirurl": "https://www.mnit.ac.in",
    "zone": "lan",
    "auth_user": USERNAME,
    "auth_pass": PASSWORD,
    "accept": "LOGIN"
}

def is_network_down():
    """Check if the network is down by pinging Google DNS (8.8.8.8)."""
    try:
        result = subprocess.run(["ping", "-n", "1", "8.8.8.8"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode != 0  # If return code is non-zero, network is down
    except Exception as e:
        print(f"⚠️ Error checking network: {e}")
        return True  # Assume network is down if there's an error

def login_to_network():
    """Send a login request to the captive portal."""
    try:
        response = requests.post(LOGIN_URL, headers=HEADERS, data=PAYLOAD)
        if response.status_code == 200:
            print("✅ Successfully logged in! Exiting script.")
            return True  # Login successful
        else:
            print(f"⚠️ Login failed with status code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error while sending login request: {e}")
    
    return False  # Login failed

def main():
    """Keep checking network status and login when needed."""
    print("🌐 Monitoring network status...")

    while True:
        if is_network_down():
            print("🚫 Network down. Trying to log in...")
            if login_to_network():
                sys.exit()  # Exit script once login is successful
            else:
                print("❌ Login attempt failed. Retrying in 5 seconds...")
                time.sleep(5)
        else:
            print("✅ Network is still up, rechecking in 1 second...")
            time.sleep(1)

if __name__ == "__main__":
    main()
