import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'janez.hagan@gmail.com'
email_password = 'sisr fayj kyhq ipzl'
email_receiver = 'janez_vegan@yahoo.com'

subject = 'Send a mail from python'
body = """
Halo

I ' ve published smo new staff
okey

LP
"""

em = EmailMessage()
em['From'] = 'janez.hagan@gmail.com'
em['To'] = 'janez.hagan@gmail.com'
em['Subject'] = "Testing gmail sending"
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
