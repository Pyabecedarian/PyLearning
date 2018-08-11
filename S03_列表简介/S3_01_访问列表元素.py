# 指出列表名称,再指出元素索引. 索引从0开始,而不是1

bicycles = ['trek', 'cannondale', 'redline', 'specilized']
print(bicycles[0])

# 使用title()让格式更加整洁

print(bicycles[0].title())


# 最后一个列表元素索引为-1

print(bicycles[-1])


# 使用拼接,根据列表中的值

print("My first bicycle was a " + bicycles[0].title())
