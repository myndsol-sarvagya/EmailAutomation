# EmailAutomation
# Mail Sender

This Python script, `mail_sender.py`, is a simple program for sending emails using the Gmail SMTP server. It allows you to specify a sender's name and a list of recipient email addresses. The script uses the `smtplib` and `ssl` libraries for secure email transmission.

## Prerequisites

Before using this script, make sure you have the following prerequisites:

1. Python 3.x installed on your system.
2. A Gmail account with two-step verification enabled.
3. App-specific password generated for your Gmail account.

## How to Use

Follow these steps to use the `mail_sender.py` script:

1. Clone or download the repository containing this script to your local machine.

2. Open the script in a code editor or text editor.

3. Replace the placeholders with your actual email information:
   - `<enter sender email address>`: Replace with your Gmail email address.
   - `<receivers email address>`: Replace with one or more recipient email addresses (comma-separated).
   - `<enter email password generated from google two-step verification>`: Replace with the app-specific password generated for your Gmail account.

4. Save your changes.

5. Open a terminal or command prompt and navigate to the directory where `mail_sender.py` is located.

6. Run the script using the following command:
   ```
   python mail_sender.py
   ```

7. The script will send an email with the specified subject and body to each recipient in the list.

8. You will see a confirmation message in the terminal for each email sent.

## Note

- Make sure to keep your email password secure and do not share it in the code or any public repository.

- You may need to allow less secure apps in your Gmail account settings to use this script. However, it is recommended to use an app-specific password for better security.

- This script sends emails using SMTP over SSL to ensure secure transmission. The default SMTP server used is `smtp.gmail.com` on port `465`.

- For any issues or questions, refer to the Python documentation for the `smtplib` library or Gmail's documentation on app-specific passwords.

**Disclaimer**: This script is provided for educational purposes and as a basic example. Please use it responsibly and in accordance with your email service provider's terms of service.
