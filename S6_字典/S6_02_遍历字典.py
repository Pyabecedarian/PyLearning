# items()方法返回一个键-值对列表

user_0 = {'username': 'efermi',
          'first': 'enrico',
          'last': 'fermi',
          }

print(user_0.items())


# 遍历字典的键-值对

for key, value in user_0.items():
    print("\nKey: " + key)
    print("\nValue: " + value)


# 更人性化的命名, 使代码更易于理解

favorite_languages = {
    'jen': 'python',
    'sarah': 'C++',
    'michael': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())

print()


# keys()方法 返回一个包含所有键的 "列表"
# TODO .keys()返回类型为 dict_keys!

# 遍历字典的所有键, 利用sorted函数对键进行排序
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")


# values()方法 返回一个值的 列表,  dict_values
# 遍历字典的所有值
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
