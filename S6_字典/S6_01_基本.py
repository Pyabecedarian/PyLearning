"""
字典  dictionary = {key1: value1, key2: value2,  ... }

key 类似于 索引, 通过 key 寻找"元素"的值
"""


alien_0 = {'color': 'green'}
print(alien_0['color'])


# 增加键-值对, 直接添加

alien_0['x_postion'] = 0
print(alien_0)


# 从空字典添加

alien_1 = {}

alien_1['color'] = 'green'
alien_1['x_position'] = 5
alien_1['x_position'] = 10  # 修改字键-值对

print(alien_1)


# del 语句 删除键-值对

del alien_1['x_position']
print(alien_1)


"""
对能够以一个不同速度移动的外星人的位置进行跟踪, 根据当前速度,
确定外星人向右移动的距离
"""

del alien_0, alien_1

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

# 像右移动外星人, 根据外星人的速度决定将其移动多远

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] += x_increment

print("New x-position: " + str(alien_0['x_position']))


# 较长的字典应放多行, print语句过长应分多行

favorite_languages = {
    'jen': 'python',
    'sarah': 'C++',
    'michael': 'ruby',
    'phil': 'python',
    }

print("Sarah's favorite languages is "
      + favorite_languages['sarah'].title() + '.')
