import fire
from getpass import getpass

def login(name=None):
    name = input("Whats Your name?\n")
    pw = getpass("What's Your Password?\n")
    print(name, pw)

if __name__ == '__main__':
    fire.Fire(login)
