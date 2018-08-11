"""
Python 使用被称为 异常 的特殊对象来管理程序执行期间的错误

使用try-except代码块让Python执行指定的操作, 同时告诉Python发生异常时
如何处理.

else代码块告诉Python在try代码块执行成功后,应接续执行的操作
"""

# 1>. 处理 ZeroDivisionError 和  ValueError 异常

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
flag = True
while flag:

    # 输入第一个整数, 不是整数重新输入
    while True:
        first_num = input("\nFirst number: ")
        if first_num == 'q':
            flag = False
            break
        try:
            first_num = int(first_num)
            break
        except ValueError:
            print("Please enter an integer number!")

    if not flag:
        break

    # 输入第二个整数, 不是整数重新输入
    while True:
        second_num = input("\nSecond number: ")
        if second_num == 'q':
            flag = False
            break
        try:
            second_num = int(second_num)
            break
        except ValueError:
            print("Please enter an integer number!")

    if not flag:
        break

    # 计算并显示结果
    try:
        ans = first_num / second_num
    except ZeroDivisionError:
        print("\tYou can't divide by 0!")
        continue
    else:
        print("Answer is : " + str(ans))

        repeat = input("Wanna try again? (yes / no): ")
        if repeat.lower() == 'no':
            flag = False


"""
注: 只要程序依赖于外部因素, 如 用户输入, 存在指定的文件, 有无网络链接,
等等, 就可能出现异常. 凭经验可判断该在程序的什么地方包含异常处理块, 
以及出现错误时该向用户提供多少相关的信息
"""
