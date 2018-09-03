"""
.format_map(d):
    Key as field name and dictionary name as argument

"""

phonebook = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'}

msg = "Cecil's phone number is {Cecil}".format_map(phonebook)
print(msg)
