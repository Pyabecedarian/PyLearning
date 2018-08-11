def count_words(f_name):
    """
    读取文本文件, 计算文件中包含单词的个数

    :param f_name: 文件名
    """

    try:
        with open(f_name, encoding='gb18030', errors='ignore') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry, the file " + f_name + " does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + f_name + " has about " +
              str(num_words) + " words.")
