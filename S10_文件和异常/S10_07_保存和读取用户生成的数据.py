"""
程序运行时, 读取用户的数据(如用户名). 若发现没有用户,
则提示用户输入用户名, 并下次登陆时无需输入

原理: 若没有存储过用户信息, 则目录内不存在 usrname.json
利用 try - except - else语句, 将读取和写入合并到一个程序

"""

import json

# 如果用户以前存储了用户名, 就加载它
# 否则, 就提示用户输入用户名并存储它
f_name = 'usrname.json'

try:
    with open(f_name) as f_obj:
        usrname = json.load(f_obj)
except FileNotFoundError:
    usrname = input("Please input your name: ")
    with open(f_name, 'w') as f_obj:
        json.dump(usrname, f_obj)
        print("We'll remember you when you come back, " +
              usrname.title() + '.')
else:
    print("Welcome back, " + usrname + '!')
