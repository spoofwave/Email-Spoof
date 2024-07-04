import requests

def send_email():
    # Prompt the user for input
    license_key = input("Enter your license key: ")
    sender_name = input("Enter sender name: ")
    sender_email = input("Enter sender email: ")
    recipient_email = input("Enter recipient email: ")
    subject = input("Enter email subject: ")
    message = input("Enter email message content: ")

    # Define the API endpoint
    url = "https://spoofwave.com/api/email"

    # Define the payload data
    data = {
        "license_key": license_key,
        "sender_name": sender_name,
        "sender_email": sender_email,
        "recipient_email": recipient_email,
        "subject": subject,
        "message": message
    }

    # Set the headers
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Make the POST request
    response = requests.post(url, data=data, headers=headers)

    # Print the response
    if response.status_code == 200:
        print("Email sent successfully!")
        print("Response:", response.json())
    else:
        print("Failed to send email.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

if __name__ == "__main__":
    send_email()
