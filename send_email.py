import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

subject = "Email From Python"
body = "This is a test email from Python!"
sender_email = "miturocks2020@gmail.com"
receiver_email = "miturocks2020@gmail.com"

# Get the email password from environment variable
password = os.getenv("EMAIL_PASSWORD")

# Create the email message
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

# Set up the SSL context
context = ssl.create_default_context()

print("Sending Email!")

# Send the email
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")
