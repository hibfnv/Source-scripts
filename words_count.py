# -*-coding:utf-8 -*-
# 定义函数变量，使用这个函数可以计算某些文本中有多少个单词。
def words_count(filename):
    """计算文件中包含了多少个单词的函数操作"""
    try:
        f = open(filename, 'r')
        content = f.read()
    except FileNotFoundError:
        notice = filename + "文件不存在，请检查文件名是否输入错误。"
        print(notice)
    else:
        words = content.split()
        num_words = len(words)
        print(words),
        print('此文件' + filename + '包含了' + str(num_words) + '个单词。\n')


filenames = {'message.txt', 'newtext.txt', 'pi_digit.txt', 'docs.txt'}
for filename in filenames:
    words_count(filename)

# 使用pass条件默认当错误发生时什么也不要做，直接跳过即可。
print("使用pass条件当错误发生里直接选择跳过错误块。\n")


def content_error(filename):
    try:
        with open(filename) as file_object:
            context = file_object.read()
            all_words = context.split()
            all_num = len(all_words)
            print(filename + "总共包含了" + str(all_num) + "个单词。")
    except FileNotFoundError:
        pass


for fn in filenames:
    content_error(fn)
