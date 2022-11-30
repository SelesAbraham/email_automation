import smtplib, ssl

receiver_email = "selessera9@gmail.com"
sender_email = "selessera9@gmail.com"
password = "******"
subject = "Weekly Maintenance"
receiver_name = "Monitoring Team"
sender_name = "SRE Team"
message = """From: {}
To: {}
Subject: {}
Hello {},

Please know that the weekly Maintenace will be due next week.

Best regards,
{}
""".format(receiver_email, sender_email, subject, receiver_name, sender_name)

# Connect to Gmail SMTP Server
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    try:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("Email was sent successfully")

    except Exception:
        print("There was an error while trying to send an Email")
