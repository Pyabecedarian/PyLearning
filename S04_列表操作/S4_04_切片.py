"""
使用列表切片可返回列表的任何子集, 只需指定索引

-1 表示列表最后一个元素
"""

players = ['charles', 'martine', 'michael', 'florance', 'ali']

print(players[1:4])  # 2~4

print(players[:4])   # 从头开始到4

print(players[1:])   # 从2到末尾

print(players[-3:])  # 从倒数第三到末尾

print(players[:])    # 从头到末尾


"""
遍历切片

for循环遍历前三名队员
"""

print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())
