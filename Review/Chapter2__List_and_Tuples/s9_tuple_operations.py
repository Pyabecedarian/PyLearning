"""
    1>  tuple():
            Works in the same way as list(), it takes one sequence argument
            and convert it to a tuple.
            If the argument is already a tuple, it is returned unchanged

"""

# Convert a list to a tuple
lst = [1, 2, 3]
print(lst)
tup = tuple(lst)
print(tup)

# Convert a string to a tuple
a_str = 'abc'
print(tuple(a_str))


"""
Two reasons for tuples:

1>  CAN be used as keys in mappings, where lists can't

2>  As RETURN values
"""