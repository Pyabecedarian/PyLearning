def count_words(filename):
    """
    读取文本文件, 计算文件中包含单词的个数

    :param filename: 文件名
    :return:
    """
    try:
        with open(filename, encoding='gb18030', errors='ignore') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry, the file " + filename + " does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " +
              str(num_words) + " words.")

