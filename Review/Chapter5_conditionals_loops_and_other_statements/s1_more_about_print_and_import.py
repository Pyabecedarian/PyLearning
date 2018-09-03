"""
1>  print():
        print more than one expression as long as you separate them
        with commas.

    print(arg1, arg2, arg3 ...)

    A space character is inserted between each argument by default,
    which can be replace by explicitly using keyword argument sep="some_str"


2>  Importing Sth as Sth Else

        from sth import sth as sth else
        import sth as sth else


3>  Sequence Unpacking

        1. assigning several different variables simultaneously
                x, y, z = 1, 2, 3

        2. switch the contents of two or more variables
                x, y = y, x

        3. packing two or more variable into a tuple
                tuple = x, y, z

        4. unpacking a sequence(or other iterable object) to some variables.
           The sequence unpacked must have exactly as many items as the targets
           listed on the left of the '=' sign.
                x, y, z = sequence




"""

# TODO  1. print multiple arguments
print('Chris', "'s", 'Age', 'is', 12)
print('Chris', "'s", 'Age', 'is', 12, sep='+', end='\n\n')


# TODO  2. sequence unpacking
values = 1, 2, 3
print(values)

x, y, z = values
print(x)

d = {'name': 'Chris', 'age': 28}
key, value = d.popitem()
print(key)
print(value)

# Instead of ensuring that the number of values matches exactly,
# can using the * operator to gather up any superfluous ones
a, b, *rest = [1, 2, 3, 4]
print(rest)

name = 'Albus Percival Wulfric Brain Dumbledore'
first, *middle, last = name.split()
print(middle)
