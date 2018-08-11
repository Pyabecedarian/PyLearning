"""
导入模块 count_words.py

分析 'Alice in Wonderland', 'Siddhartha', 'Moby Dick'
和 'Little Women'分别包含多少个单词
    (将随意一篇文章放在 word_count.py 所在目录外)
"""
from S10_文件和异常.count_words import count_words

file_names = ['Alice in Wonderland.txt', 'Siddhartha.txt',
              'Moby Dick.txt', 'Little Women.txt']

for file_name in file_names:
    count_words(file_name)
