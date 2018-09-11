# 使用open函数来进行文件的创建和查看，w为写入文件，r为读取文件，a为追加在文件末尾,b为以二进制的形式查看或\
# 读写(可追加到其它的模式),+为读写模式(可追加到其它模式中)
# -*-coding:utf-8 -*-
print('以open(file)赋值形式创建读写文件。')
f = open('message.txt', 'w')
f.write("This is a test message.")
f.close()
print('\n')
print('以with open形式来创建或读写文件。')
filename = 'newtext.txt'
with open(filename,'w') as file_object:
    file_object.write("For the first test text content, I was so glad!\n")
    file_object.write("This is very strange feel that I've never touch before.\n")