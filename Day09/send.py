import sys
from datetime import datetime
import fire
from formatting import format_msg
from send_mail import send_mail

def get_name():
    name = fire.Fire(input("Recipient: "))
    return name

def send(name, website=None, verbose=False):
    if website != None:
        msg = format_msg(my_name=name, my_website=website)
    else:
        msg = format_msg(my_name=name)
    if verbose:
        print(name, website)
    try:
        send_mail(text=msg)    
        sent= True
    except:
        sent = False
    return sent

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = get_name()
    response = send(name, verbose=False)
    print("Sent:", response, "\nTo:", name)