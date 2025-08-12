import smtplib
from email.message import EmailMessage
import json

with open("config.json") as f:
    config = json.load(f)

# Open the plain text file whose name is in textfile for reading.

textfile = "/home/mhsn/Desktop/automation/test.txt"

with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'The contents of {textfile}'
msg['From'] = config["sender"]
msg['To'] = config["receiver"]

my_email = config["gmail_user"]
app_password= config["gmail_pass"]

    # SMTP Server and port no for GMAIL.com
gmail_server= "smtp.gmail.com"
gmail_port= 587


    # Starting connection
my_server = smtplib.SMTP(gmail_server, gmail_port)
my_server.ehlo()
my_server.starttls()

# Login with your email and password
my_server.login(my_email, app_password)

my_server.send_message(msg)
my_server.quit()