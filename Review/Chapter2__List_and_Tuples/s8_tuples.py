"""
Tuples are sequences, like lists, but immutable(can't be changed)

    1>  Syntax
"""


# TODO  1. Syntax: Separate some values with commas

x = 1, 2, 3
print(x)

x = (1, 2, 3)
print(x)

# Empty tuple
x = ()
print(x)

# A single-value tuple include a comma
x = (42, )
print(x)

int_num = (42)
print(int_num, end='\n\n')

# Without a comma, change the value of an expression completely
x = 3 * (40 + 2)
print(x)
y = 3 * (40 + 2,)
print(y, end='\n\n')
