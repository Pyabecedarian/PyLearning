"""
当需要在字典中将一个键关联多个值时,可以在字典中嵌套一个列表

要描述顾客店的比萨, 使用字典储存要添加的配料列表, 并包含其他的披萨信息

pizza = {'crust' : 'thick',
        'toppings: '[..., ..., ...]'}
"""

# 存储披萨的信息
pizza = {'crust': 'thick',
         'toppings': ['mushrooms', 'pepperoni', 'extra cheese']}

# 概述比萨的信息
print("You ordered a " + pizza['crust'] + "-crust pizza" +
      " with following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
print()


"""
每个被调查者相关联的都是一个语言列表, 而不是一种语言.

使用for 循环遍历
"""


favorite_languages = {'jen': ['python', 'c', 'ruby'],
                      'sarah': ['c++'],
                      'michael': ['java', 'go'],
                      'phil': ['python', 'c++'],
                      }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(name.title() + "'s favorite language is:" )
    else:
        print(name.title() + "'s favorite languages are:")
    for language in languages:
        print('\t' + language.title())
    print()
