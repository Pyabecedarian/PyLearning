"""
读取整个文件

读取 pi_digits.txt 文件, 将其内容显示到屏幕
"""


# 相对路径 (在当前模块所在目下查找)
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())
# print()
# 绝对路径
"""
windows中路径使用backslash(\)隔开, 而python将其视为转义字符
因此应采用\\而不是\, 否则将会报错
"""
# file_path = 'C:\\Users\\Liu-q\\OneDrive\\Documents\\myProject\\S10_文件和异常\\pi_digits.txt'
#
# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(contents)


"""
逐行读取文件
"""

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())
# print()

"""
创建一个包含文件内容的列表

要在with代码块外访问文件的内容, 可在with内将文件的各行存储在一个列表中
"""

# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# for line in lines:
#     print(line.rstrip())
# print()


# # 使用文件中的内容
# # 创建一个字符串, 包含文件中存储的所有数字, 且没有任何空格:

# with open(filename) as file_object:
#     lines = file_object.readlines()
#     pi_string = ''
#     for line in lines:
#         pi_string += line.strip()
#
#     print(pi_string)
#     print(len(pi_string))


"""
读取pi小数点后100万, 存入字符串中,并打印

pi_million_digits.txt

"你的生日在pi中吗??"
"""

file_name = "pi_million_digits.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()

    print("The length of 'pi_string' is : " + str(len(pi_string)))
    print()
    print(pi_string)


# Birthday in PI(first million digits)?

is_continue = True

while is_continue:
    birthday = input("Enter your birthday, in the form mmddyy: ")

    if birthday in pi_string:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does not appear in the first million digits"
              " of pi.")

    while True:
        repeat = input("\nDo you want to try again? (yes / no) :")
        if repeat.lower() == 'no':
            is_continue = False
            break
        elif repeat.lower() == 'yes':
            break
        else:
            print("Please enter 'yes' or 'no'.")
