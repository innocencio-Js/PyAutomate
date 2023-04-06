import smtplib
import os
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
 
sender_email = "Sender"
recipient_email = "Reciever"
cc_email = "Reciever CC"

msg = MIMEMultipart()

msg['Subject'] = "Automated Mail"

msg['From'] = sender_email
msg['To'] = recipient_email
msg['Cc'] = cc_email

today_date = datetime.date.today().strftime('%d%b')
attachment_path = r"C:\Users\OneDrive\Desktop\PyAutomate\Notepad{}.txt".format(today_date)

with open(attachment_path, 'rb') as f:
    attachment_data = f.read()

attachment = MIMEApplication(attachment_data, _subtype='txt')
attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))

msg.attach(attachment)

smtp_server = "smtp.office365.com"
smtp_port = 587
smtp_username = "Sender Email Address"
smtp_password = "Sender Email Password"

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
