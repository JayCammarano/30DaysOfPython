while True:
    name = input("what's your name\n")
    if name != None and name != "":
        break
    else:
        tried +=1
    if tries > 10:
        break
    else:
        continue
print('hello', name)
from getpass import getpass
pw = getpass("what's your password")
