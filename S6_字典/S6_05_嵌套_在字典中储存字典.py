"""
在字典储存字典, 代码可能很快复杂起来. 应使字典中的每个字典的结构
保持一致, 使代码清晰易懂.

例: 利用字典嵌套字典, 保存网站的多个用户, 每个用户名作为键, 对应
的值是一个字典, 该字典保存每个用户的多个信息, 包括名, 姓和居住地,
利用for循环遍历输出每个用户的信息.

dict_dict = {key1: {key11: value11,
                    key12: value12,
                    ... ...},

             key2: {key21: value21,
                    key22: value22,
                    ... ...},

             ... ...
             }
"""

users = {
    'asinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },

    'lchris': {
        'first': 'liu',
        'last': 'chris',
        'location': 'beijing',
    },

}

for username, user_info in users.items():
    print("\nUsername: " + username)

    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
