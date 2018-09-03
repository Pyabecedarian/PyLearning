"""
0>  list():
1>  Item Assignment
2>  Item Deletion

    3>  Slice Assignment

4>  list methods
"""

# TODO:  3. Assigning to Slice
name = list('Perl')
print(name)

name[2:] = list('ar')  # Assigning to slice with a sequence of same length
print(name)

# Also, can replace the slice with a sequence whose length is different
name = list('Perl')
print(name)
name[1:] = list('ython')
print(''.join(name))

# Slice assignment can be used to INSERT elements without replacing any of the original ones
numbers = [1, 5]
numbers[1:1] = list('234')
print(numbers)

# 'Replace' an empty slice: Do the reverse to delete a slice
numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers[1:4] = []
print(numbers)
