import imaplib
import email
from dotenv import load_dotenv
from os import environ

from send_mail import send_mail

load_dotenv()

host = 'imap.gmail.com'
my_username = environ.get('USERNAME')
my_password = environ.get('PASSWORD')

def get_inbox(username=my_password, password=my_password):
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")

    _, search_data = mail.search(None, 'UNSEEN')
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject', 'to', 'from', 'date']:
            print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]
            email_data['body'] = body.decode()
        for part in email_message.walk():
            if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
                body = part.get_payload(decode=True)
                print("Message Body:", body.decode())
            else:
                print(part.get_content_type())

if __name__ == '__main__':
    send_mail(my_username, my_username, my_password, to_emails=[my_username])
    get_inbox(my_username, my_password)
