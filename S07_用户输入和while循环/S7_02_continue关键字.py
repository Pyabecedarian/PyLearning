"""
与 break 不同, continue关键字可返回至循环开头, 重新测试条件

输入 1 ~ 10 之间的偶数, 使用while循环
"""

current_num = 2
while current_num <= 10:
    current_num += 1  # 忘记修改计数器将导致无限循环
    if current_num % 2 != 0:
        continue

    print(current_num)
