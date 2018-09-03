"""
    1>.  Indexing

2>.  Slicing
3>.  Adding
4>.  Multiplying
5>.  Membership
"""

# TODO:  1. Indexing
greetings = 'Hello'
print(greetings[0])
print(greetings[-1])

# Indexing directly without using a variable to refer to them
print('Hello'[1])       # 'e'

# Indexing directly after a function call which returns a sequence
fourth = input('Year: ')[3]
print(fourth)           # '5'  << '2005'

"""
Listing 2-1

Print out a date, given year, month, and day as numbers
"""

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# A list with one ending for each number from 1 to 31
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
    + ['st', 'nd', 'rd'] + 7 * ['th'] \
    + ['st']

year = input('Year: ')
month = input('Month (1-12): ')
day = input('Day (1-31): ')

month_number = int(month)
day_number = int(day)

# Remember to subtract 1 from month and day to get a correct index
month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]

print(month_name + ' ' + ordinal + ', ' + year)
