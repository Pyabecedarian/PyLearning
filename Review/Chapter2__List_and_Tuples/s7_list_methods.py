"""
List Method:    (SIMILARITY: MODIFIES THE LIST DIRECTLY)

1>  .append():
        Not SIMPLY return a new, modified list;
        instead, it modifies the old one directly

2>  .clear()
        Clears the contents of a list, in place

3>  .copy()
        Copy a list.
        RECALL: the '=' assignment simply binds another name to the same list

4>  .count()
        Count the occurrences of an element in a list


5>  .extend()
        Append several values by supplying a sequence of values

6>  .index()
        Search list to find the index of the FIRST occurrence of a value

7>  .insert()
        Insert an object into a list

8>  .pop()
        Remove the element(by default, the last one) from the list,
        and returns it

9>  .remove()
        Remove the FIRST occurrence of a value

10>  .reverse()
        Reverse the elements in the list

11>  .sort()
        Used to sort list in place in a particular order,
        rather than simply returning a sorted copy of the list.

        **If want a sorted copy of a list while leaving the original one,
        use sorted() function.**

"""


# TODO  1. append()
lst = [1, 2, 3]
print(lst)
lst.append(4)
print(lst, end='\n\n')


# TODO  2. clear()
lst = [1, 2, 3]
lst.clear()  # Similar to the slice assignment, lst[:] = []
print(lst, end='\n\n')


# TODO  3. copy()
a = [1, 2, 3]
b = a
print(a)
b[1] = 4  # Assigning a element using 'b' list
print(a, end='\n\n')  # 'a' list literally changed


# TODO  4. count()
lst = ['to', 'be', 'or', 'not', 'to', 'be']
print(lst.count('to'))

x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print(x.count(1))           # NOTICE: returns 2
print(x.count([1, 2]), end='\n\n')      # NOTICE: returns 1


# TODO  5. extend()
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)     # Notice the difference against concatenation
print(a)

a = [1, 2, 3]
b = [4, 5, 6]
a[len(a):] = b  # SAME THING:  Assigning to slice
print(a, end='\n\n')


# TODO  6. index()
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
index = knights.index('who')
print(index)


# TODO  7. insert()
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print(numbers)

numbers = [1, 2, 3, 5, 6, 7]
numbers[3:3] = ['four']  # SAME THING: Assigning to slice
print(numbers, end='\n\n')


# TODO  8. pop()
x = [1, 2, 3]
x.pop()
print(x)
x.pop(0)
print(x)

# NOTICE: the pop() and append() methods reverse each other's results
x = [1, 2, 3]
print(x)
x.append(x.pop())
print(x, end='\n\n')


# TODO  9. remove()
lst = ['to', 'be', 'or', 'not', 'to', 'be']
lst.remove('be')  # NOTICE: return nothing
print(lst, end='\n\n')


# TODO  10. reverse()
x = [1, 2, 3]
print(x)
x.reverse()
print(x, end='\n\n')


# TODO  11. sort()
x = [4, 6, 2, 1, 7, 9]
print(x)
x.sort()
print(x)

# sort a copy of the list
x = [7, 8, 2, 1, 4, 3]
y = x.copy()
y.sort()
print(x)
print(y)

# sorted() can be used on any sequence but will always return a list
y = sorted('Python')
print(y, end='\n\n')


"""
Advanced Sorting

.sort() takes two optional arguments:
    1. key
    2. reverse
    
1. key: supply a function (eg. len)
2. reverse: True/False
"""

# Sorting the elements according to their lengths, reversely
x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len, reverse=True)
print(x)
