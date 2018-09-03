"""
1>.  Indexing
2>.  Slicing
3>.  Adding
4>.  Multiplying

    5>.  Membership
"""

# TODO:  5. Check whether a value can be found in a sequence
permissions = 'rw'
print('w' in permissions)
print('x' in permissions)

print()

users = ['mlh', 'foo', 'bar']
print(input('Enter your user name: ') in users)

print()


"""Listing 2-4

Check a user name and PIN code 
"""

database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]

username = input("User name: ")
pin = input('PIN code: ')

if [username, pin] in database: print('Access granted')
