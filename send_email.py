import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "bacovska.marcela@gmail.com"
password = "gotu fhif ejim heqi"

receiver = "bacovska.marcela@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Portfolio website message 
HI!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

