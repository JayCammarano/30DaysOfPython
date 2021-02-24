import sys
if __name__ == "__main__":
    try:
        name = sys.argv[1]
        print(name)
    except:
        name = input("what's your name\n")
    print(name)
