"""
复制列表

使用包含整个列表的切片 来复制列表, 即
copy_list = list[:]

注: 不能使用 copy_list = list, 这种语法只是给list取了个别名

"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
friend_foods_test = my_foods

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)

print("\nNow I add 'ice cream' in my favorite foods list, then")
my_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend favorite foods are:")
print(friend_foods)

print("\n'test' suffixed food list are literally the same as mine:" )
print(friend_foods_test)
