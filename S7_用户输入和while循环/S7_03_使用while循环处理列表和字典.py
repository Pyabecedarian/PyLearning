"""
在列表之间移动元素

for循环遍历列表时, 不应修改列表.
要在遍历列表时同时对其修改, 可使用while循环.

例如: 假设有一个列表, 储存了新注册但还未验证的网站用户;
验证这些用户后, 将他们移动到另一个已验证用户的列表中.

使用while循环, 在验证用户的同时将其从未验证用户列表中提取出来
"""

# 首先, 创建一个待验证的用户列表
# 和一个用户存储已验证用户的列表

unconfirmed_users = ['alice', 'sarah', 'rain', 'phil']
confirmed_users = ['chris']

while unconfirmed_users:  # 重要: 列表为空时终止循环
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title() + '...')
    confirmed_users.append(current_user)

# 显示所有已验证用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print("\t%s" % confirmed_user.title())


"""
使用用户输入来填充字典

使用while循环提示用户输入任内亦数量的信息.

例如: 循环每次执行都提示被调查中输入姓名和回答. 将收集的数据储存在字典中,
以便将回答同被调查者联系起来.

"""
responses = {}
while True:
    name = input("\nWhat's your name: ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? "
                   "(yes/ no) ")
    if repeat.lower() == 'no':
        break

print("\n\n--- Polling Results ---")
for name, response in responses.items():
    print(name.title() + ' would like to climb ' + response.title() +
          '.')
