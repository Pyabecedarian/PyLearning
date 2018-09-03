"""
1>  dict():

        1. Construct dictionaries from other mappings or
        from sequences of (key, value) pairs

        2. Use keyword arguments


2>  Basics:
        1. len(d):
            returns the number of items in d

        2. d[k]: returns the value associated with the key k

        3. del [k]: deletes the item with key k

        4. k in d checks whether there is an item in d has the key k

"""

# 1.1 Construct dictionary from (key, value) pairs
items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print(d)

# 1.2 Using keyword arguments explicitly
d = dict(name='Chris', age=29)
print(d)


"""
Sample 4-1:  A simple database

A dictionary with person names as keys. Each persion is represented
as another dictionary with the keys 'phone' and 'addr' referring to
their phone number and address, respectively
"""

people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },

    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },

    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }

}

# Descriptive labels for the phone number and address.
# Will be used when printing the output.
labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('Name: ')

# Are we looking for a phone number and an address?
request = input('Phone number (p) or address (a)?')

# Use the correct key:
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'

# Only try to print information if the name is a valid key
# in our dictionary
if name in people:
    print("{}'s {} is {}.".format(name,
                                  labels[key],
                                  people[name][key]))
