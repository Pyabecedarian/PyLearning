"""
一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序:
1> 完成随机的分配
2> 获取办公室信息 (每个办公室中的人数，及分别是谁)
"""

from random import randint

teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = []

# 创建 办公室列表(列表嵌套)
i = 0
while i < 8:
    offices.append([])
    i += 1

# 1>. 完成随机分配, 将老师随机分配到某个办公室中
for teacher in teachers:
    i = randint(0, (len(offices)-1))
    office = offices[i]
    office.append(teacher)

print(offices)

# 2>. 获取办公室信息
i = 1
for office in offices:
    print("第%d 个办公室中有 %d 个老师." % (i, len(office)))
    i += 1
    for teacher in office:
        print(teacher)
