"""
文本分析 --- 获取文章 "Alice in Wonderland" 中的单词个数

str.split()以空格为分隔符将字符串拆分成多个部分(可能包含标点符号),
并将这些部分储存在一个列表中.

采用try-except-else处理 FileNotFoundError 异常

完成功能后封装到函数中
"""

# 读取 'Alice in Wonderland.txt'
file_name = "Alice in Wonderland.txt"
try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file \"" + file_name + "\" has about " +
          str(num_words) + " words.")
