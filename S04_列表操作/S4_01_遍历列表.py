# for 循环遍历列表

magicians_list = ['alice', 'david', 'carolina']

for magician in magicians_list:
    print(magician.title() + ', that was a great trick!')
    print("I can't wait to see your next trick, " + magician.title()
          + '\n')

print("Thank you, everyone. That was a great magic show!")
