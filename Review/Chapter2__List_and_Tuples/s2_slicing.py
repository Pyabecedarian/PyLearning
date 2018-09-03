"""
1>.  Indexing

    2>.  Slicing

3>.  Adding
4>.  Multiplying
5>.  Membership
"""

# TODO:  2 Slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:6])

# Access the last three elements of numbers
print(numbers[7:10])    # √, Index 10 does no exist
print(numbers[-3:-1])   # ×,
print(numbers[-3:0])    # ×, Empty list
print(numbers[-3:])     # √, Correct way

# Extracting elements from right to left
print(numbers[10:0:-2])

"""
Listing 2-2

Split up a URL of the form http://www.something.com
"""

url = input('Please enter the URL: ')
domain = url[11:-4]

print("Domain name: " + domain)


