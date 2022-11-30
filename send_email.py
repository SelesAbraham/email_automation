import smtplib, ssl
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-s", "--sender-email", dest="sender_email", default=None)
parser.add_argument("-p", "--sender-password", dest="sender_password", default=None)
parser.add_argument("-r", "--receiver-email", dest="receiver_email", default=None)
parser.add_argument("-su", "--subject", dest="subject", default=None)
parser.add_argument("-rn", "--receiver-name", dest="receiver_name", default=None)
parser.add_argument("-sn", "--sender-name", dest="sender_name", default=None)
parser.add_argument("-m", "--message", dest="message", default=None)
args = parser.parse_args()

receiver_email = args.receiver_email
sender_email = args.sender_email
sender_password = args.sender_password
subject = args.subject
receiver_name = args.receiver_name
sender_name = args.sender_name
message = args.message
print(f"receiver_email: {receiver_email}, sender: {sender_email}, password: {sender_password}")
content = """From: {}
To: {}
Subject: {}
Hello {},

{}

Best regards,
{}
""".format(receiver_email, sender_email, subject, receiver_name, message, sender_name)

# Connect to Gmail SMTP Server
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    try:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, content)
        print("Email was sent successfully")

    except Exception as e:
        print(f"There was an error while trying to send an Email: {e}")
