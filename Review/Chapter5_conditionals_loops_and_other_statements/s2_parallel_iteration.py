"""
1>  zip():
    zips together the sequences, returning a sequence of tuples


2>  enumerate():

"""


names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]

z = zip(names, ages)
print(z)
print(list(z), end='\n\n')

for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')

print()


# enumerate()
strings = ['alice', 'anne', 'sarah', 'phil', 'george', 'damon']
print(strings)
for index, string in enumerate(strings):
    if 'sarah' in string:
        strings[index] = 'chris'
print(strings)
print(list(enumerate(strings)))

