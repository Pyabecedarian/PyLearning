"""
创建一个循环, 接受用户姓名, 并打招呼. 当用户输入"q"时退出循环

导入 get_formatted_name 函数
"""

import S8_函数.functions_

while True:

    print("\nPlease tell me your name:")
    print("\t(enter 'q' at any time to quit)\n")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = S8_函数.functions_.get_formatted_name(f_name, l_name)
    print("\nHello, " + str(formatted_name) + "!")
