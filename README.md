# Email Spoofer

This Python script allows you to send spoofed emails using the SpoofWave API. It prompts the user for necessary details such as license key, sender name, sender email, recipient email, subject, and message content, and then sends an email with the provided details.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository or download the `spoofemail.py` script.

2. Install the required Python library:
    ```bash
    pip install requests
    ```

## Usage

1. Run the script from the command line:
    ```bash
    python3 spoofemail.py
    ```

2. Enter the required details when prompted:
    - License key (can be purchased from [SpoofWave](https://spoofwave.com/buy/email))
    - Sender name
    - Sender email
    - Recipient email
    - Email subject
    - Email message content

3. The script will send the email using the provided details and print the response from the API.

## Example

```bash
$ python3 spoofemail.py
Enter your license key: your_license_key
Enter sender name: John Doe
Enter sender email: john.doe@example.com
Enter recipient email: jane.doe@example.com
Enter email subject: Test Email
Enter email message content: This is a test email.

Email sent successfully!
Response: { ... }
