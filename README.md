# Captive-Portal-Auto-Login
A small python script to automatically login to the captive portal in the MNIT J's internet login portal.

NOTE : Works in  <b>Windows</b> only for now

## Pre-Requisites:
Selenium library for Python (install using `$ pip install selenium`)<br>
Edge web browser <br>
(You use can ChatGPT to modify the code for your web browser)

## Usage:
### 1. Open login.py in a text editor

Replace "id" & "password" with your username/id and password.

Save and exit.

### 2. Open autologin.bat in a text editor
Replace /"pathto" /python.exe with the path to python interpreter in your PC.

Replace /"pathto" /login.py with the path to login.py in your PC.

Save and exit.

### NOTE: To Find out the path to your python executable
Type `python -c "import sys; print(sys.executable)"` in your cmd / powershell 


### Enjoy !!
Now whenever you want to log-on, double click autologin.bat  







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
- Choose **Daily** and set the **Start time** to `12:00 AM`.
- Click **OK**.

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
