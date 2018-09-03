"""
Match the boys and girls with the same character in front
"""

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']

matches = [b + '+' + g for b in boys for g in girls if b[0] == g[0]]
print(matches)
print()
"""
The comprehension works, but not that efficiency, cuz each iteration
step in boys contains the full iteration in girls.
"""


# A Better Solution
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']

letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)

matches = [b + '+' + g for b in boys for g in letterGirls[b[0]]]
print(matches)


# TODO  dictionary comprehension
squares = {i:'{} square is {}'.format(i, i**2) for i in range(10)}