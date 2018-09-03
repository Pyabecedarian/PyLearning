"""
Sample 4-2

Modified version of Sample 4-1
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

labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input("Name: ")

# Are we looking for a phone number or an address?
request = input('Phone number (p) or address (a)? ')
key = request  # In case request neither p nor a
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

print("{}'s {} is {}".format(name, label, result))