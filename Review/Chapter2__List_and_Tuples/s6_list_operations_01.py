"""
    0>  list():
            As strings can't be modified in the same way as lists,
            sometimes it can be useful to create a list from a string

    1>  Item Assignment

    2>  Item Deletion

3>  Slice Assignment
4>  list methods
"""

# TODO:  0. list()

a_string = 'Hello, Python'
list_a_string = list(a_string)
print(list_a_string)  # NOTE: list works with all kinds of sequences, not just strings

#  Convert a list of characters back to a string
back_a_string = ''.join(list_a_string)
print(back_a_string)


# TODO:  1. Changing lists: Item Assignment
x = [1, 1, 1]
print(x)
x[1] = 2
print(x)


# TODO:  2. Deleting Elements: del
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
print(names)
del names[2]
print(names)
