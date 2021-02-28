import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from os import environ

load_dotenv()
my_username = environ.get('USERNAME')
my_password = environ.get('PASSWORD')


def send_mail(from_email=my_username, username=my_username, password=my_password, text='Email Body', subject="Hello World", to_emails=[my_username], html=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To:'] =  ", ".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    if html != None:
        html_part = MIMEText("<h1>This is working</h1>", 'html')
        msg.attach(html_part)
    msg_str = msg.as_string()

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()

if __name__ == '__main__':
    send_mail(my_username, my_username, my_password, to_emails=[my_username])
