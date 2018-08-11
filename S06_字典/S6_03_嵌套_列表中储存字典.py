"""
字典列表: 在列表中储存字典

可用于储存一系列包含多个属性的变量集合, 例如:

1> 生成一个包含30个外星人的列表, 每个外星人包括多个属性, 均采用一个
独立的字典进行存储

2> 批量修改前5个外星人得到属性
"""

aliens = []

for alien_num in range(0, 6):
    new_alien = {'color': 'green', 'points': 20, 'speed': 'medium'}
    aliens.append(new_alien)

# 修改前5个外星人的属性, 变黄色/速度为中
print("修改前:")
for alien in aliens[:5]:
    print(alien)

print("修改后:")
for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'fast'
        alien['points'] = 30
    elif alien['color'] == 'yellow':
        alien['color'] = 'green'
        alien['speed'] = 'medium'
        alien['points'] = 20
    print(alien)
