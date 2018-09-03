"""
1>  .clear():
        Removes all items from the dictionary


2>  .copy():
    Returns a new dictionary with the same key-value pairs.
    BUT, .copy() is essentially a shallow copy, since the values
    themselves have the same address

    To avoid this problem, use  .deepcopy() instead


3>  .fromkeys():
    Create a new dictionary with the given keys and set default value
    to None.


4>  .get():
        Accessing an dictionary items, if the items not in it, returns
        default value None, or customized value


5>  .items():
        Return all the items of a dictionary as a list of items(dictionary view)
        in which each items is of the form (key, value).
        The order of items is unpredictable.


6>  .keys():
        Works the same way as .items(), which returns all the keys of
        a dictionary as a list

    APPENDIX: .values()


7>  .pop():
        Used to get the value corresponding to given key then to remove
        the key-value pair from the diciontary


8>  .popitem():
        Works similar to list.pop(), which pops off the last element of
        a list. However, popitem() pops off a arbitrary item as dictionay
        don't have a "last element" or any order whatsoever.


9>  .setdefault()
        Similar to .get(). However setdefault() sets the value corresponding
        to the given key if it's not already in dictionary


10>  .update()
        Update a dictionary with the items of a mapping / a sequence / (or
        other iterable object) of (key, value) pairs, or keyword arguments
"""


# TODO  1. clear()
d = {}
print(d)
d['name'] = 'Gumby'
d['age'] = 42
print(d)
d.clear()
print(d, end='\n\n')


# TODO  2. copy()
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
print(x)
print(y)
y['username'] = 'mlh'
y['machines'].remove('bar')
print(y)
print(x, end='\n\n')

# To avoid this problem, can make a deep copy by using deepcopy()
from copy import deepcopy
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
yc = x.copy()
ydc = deepcopy(x)
ydc['machines'].remove('bar')
print(x)
print(ydc, end='\n\n')


# TODO  3. fromkeys()
d = {}
d_c = d.fromkeys(['name', 'age'])
print(d)
print(d_c)

# Can also set customized value corresponding to the given keys
d_c = d.fromkeys(['name', 'age'], 'unknown')
print(d_c, end='\n\n')


# TODO  4. get()
d = {'age': 18}
print(d.get('name', 'N/A'))
print(d.get('age'), end='\n\n')


# TODO  5. items()
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.items())
# .iterms() 's return value called dictionary view, which can always
# reflect the underlying dictionary, even if you modify it.
d['spam'] = 1
print(('spam', 1) in d, end='\n\n')


# TODO  7. pop()
d = {'x':1, 'y':2}
print(d.pop('x'))
print(d, end='\n\n')


# TODO  9. setdefault()
d = {}
print(d.setdefault('name', 'N/A'))
print(d)
d['name'] = 'Chris'
print(d.setdefault('name', 'N/A'))
print(d, end='\n\n')


# TODO  10. update()
d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'
}

x = {'title': 'Python Language Website'}
d.update(x)
print(d)
x = [('changed', 'June 15 20:00 MET 2017')]
d.update(x)
print(d)
x = (('changed', 'October 01 07:00 MET 2018'),)
d.update(x)
print(d)
d.update(title='Python Official Website')
print(d)
