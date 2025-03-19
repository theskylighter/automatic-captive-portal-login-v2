# Captive-Portal-Auto-Login

A simple Python script to automatically log in to the captive portal for MNIT Jaipur's internet service using HTTP requests and network monitoring.

**NOTE :** `.bat` files are windows specific. For linux/mac users, you can use crontab to schedule the script to run at a specific time.

## Pre-Requisites:
- Python 3.x installed on your machine.
- Python package: `requests` (Install using: `pip install requests`)

## Setup Instructions:

1. Clone the repository to your local machine.
2. Open `login.py` in a text editor and replace the placeholder credentials with your actual campus network login details. For example:
    ```python
    USERNAME = "your_username"
    PASSWORD = "your_password"
    ```
3. Open `autologin.bat` in a text editor.
4. Replace `"pathTo\python.exe"` with the full path to your Python interpreter. Example:
    ```
    "C:/Users/YourUsername/AppData/Local/Programs/Python/Python39/python.exe"
    ```
    or just write
    ```python3```

5. Replace `"pathTo\login.py"` with the full path to the `login.py` script on your system. For example:
    ```
    "D:/codes/captive-LOGIN/automatic-captive-portal-login-v2/login.py"
    ```
6. Save the files.

## How It Works:

- The script continuously monitors your network connectivity by pinging Google's DNS server (8.8.8.8).
- When the network is detected as down, it sends a POST request to the captive portal login URL with your provided credentials.
- If the login is successful, the script exits; otherwise, it retries after a short delay.
  
**MAC/Linux Note:**  
The current network check in `login.py` uses the Windows-specific ping flag `-n`. If you wish to run this script on macOS or Linux, update the `is_network_down()` function to use the `-c` flag instead of `-n`.

### Enjoy!
Now, whenever you need to log in, just double-click `autologin.bat` or rely on Task Scheduler for automated login.

## Steps to Further Automate Your Batch File Using Task Scheduler

You can automate the batch file execution at 12 AM using Task Scheduler on Windows. This way, the batch file will run automatically without needing manual intervention.

### 1. Create a Task in Task Scheduler:

- **Open Task Scheduler**: Press `Win + S`, type "Task Scheduler," and press Enter.
- In the Task Scheduler window, click on **Create Task** in the right panel.

### 2. General Settings:

- In the **General** tab, give the task a name (e.g., "Campus Network Login").
- Choose **Run whether user is logged on or not** to ensure the task runs even when you're not actively using the computer.
- Check **Run with highest privileges** if admin access is required.

### 3. Triggers (Setting up the time):

- Go to the **Triggers** tab and click **New**.
- Set **Begin the task** to **On a schedule**.
- Choose **Daily** and set the **Start time** to `12:00 AM`. (12:01 AM Preferred)
- Click **OK**.

(optional) Trigger 2
- Go to the **Triggers** tab and click **New**.
- Set **Begin the task** to **At start up**.
- Tick box Stop task id it runs longer than -10 min 

### 4. Actions (Run the batch file):

- Go to the **Actions** tab and click **New**.
- In the **Action** dropdown, select **Start a program**.
- In the **Program/script** field, browse for the `.bat` file that you created to run your Python script.
- Click **OK**.

### 5. Conditions and Settings (Optional):

- In the **Conditions** tab, you can add extra conditions, like running the task only if the computer is idle, or waking the computer to run the task.
- In the **Settings** tab, you can allow the task to be retried if it fails and stop the task if it runs too long.

### 6. Save the Task:

- Click **OK** to save the task.
- When prompted, enter your Windows account password (this is required if you set it to run whether you're logged on or not).

## FAQ

### 1. How do I clone this repository?
Cloning a repository allows you to download the code and work on it locally. Here are the steps:

- Open Git Bash (or any terminal you're comfortable with).
- Navigate to the directory where you'd like to clone the repository using the `cd` command. Example:
    ```bash
    cd D:/codes/GIT Clones
    ```
- Use the `git clone` command followed by the repository URL:
    ```bash
    git clone https://github.com/theskylighter/automatic-captive-portal-login.git
    ```
- Once cloned, navigate to the cloned folder:
    ```bash
    cd automatic-captive-portal-login
    ```
Now you're all set to work with the project!

### 2. How do I find the path to my Python interpreter?
To find the path to your Python executable, open your Command Prompt or PowerShell and run the following command:

```bash
    python -c "import sys; print(sys.executable)" 
```

This will output the exact path where Python is installed on your machine.


