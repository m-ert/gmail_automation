import smtplib
from email.message import EmailMessage
import json
import csv
import time
import mimetypes

with open("config.json") as f:
    config = json.load(f)

# Open the plain text file whose name is in textfile for reading.
textfile = "/home/mhsn/Desktop/automation/test.txt"
resume = "/home/mhsn/cv/Muhsin_Ertekin.pdf"

ctype, encoding = mimetypes.guess_type(resume)
if ctype is None or encoding is not None:
    ctype = 'application/octet-stream'  # default type for unknown files

maintype, subtype = ctype.split('/', 1)

with open(resume, 'rb') as f:
    resume_data = f.read()


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

with open('list.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        cur_address = lines[0]

        # Create new message per recipient
        msg = EmailMessage()
        with open(textfile) as fp:
            msg.set_content(fp.read())

        msg['From'] = config["sender"]
        msg['To'] = cur_address
        msg['Subject'] = f"Staj Başvurusu"
        msg.add_attachment(resume_data, maintype=maintype, subtype=subtype, filename="Muhsin_Ertekin.pdf")

        my_server.send_message(msg)
        print(f"Mail sent to {cur_address} successfully")
        time.sleep(10)

my_server.quit()