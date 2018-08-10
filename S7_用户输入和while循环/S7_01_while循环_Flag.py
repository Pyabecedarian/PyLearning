# 使用while循环, 保持程序一直运行. 使用 函数input() 接受用户的输入,
# 屏幕显示用户输入的内容. 当用户输入'quit' 退出程序

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\n (Enter 'quit' to end the program.)\n"

while True:
    message = input(prompt)
    if message == 'quit':
        break  # 使用 break 退出循环
    print("\nWhat message you type is: \n\t" + message)


"""
使用[标志 Flag], 保持循环的运行

这样在程序中, 任何要导致循环终止的事件,只要将标志设置为False即可停止循环

格式:

is_active = True

while is_active:
    message = input(prompt)
    
    if message = 'quit'
        is_active = False
    else:
        print(message)

"""
