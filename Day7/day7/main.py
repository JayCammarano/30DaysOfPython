def my_print(txt):
    print(txt)

my_print("Hello world")

msg_template = """Hello {name},
Thank you for joining {website}. 
We are very happy to have you with us.
""" #.format(name="Justin", website='cfe.sh')

def format_msg(name="Justin", website="cfe.sh"):
    my_msg = msg_template.format(my_name=name, my_website=website)
    # print(my_msg)
    return my_msg

