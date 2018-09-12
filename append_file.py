# -*-coding:utf-8 -*-
# Author: Eason
filename = 'message.txt'
with open(filename, 'w') as file_object:
    file_object.write("This is a very simple sentence which we used to test the file open method.\n")

with open(filename, 'a') as f_obj:
    f_obj.write("Hallo, welcome to test the script.\n")


fn = open(filename, 'a')
fn.write("How funny it is, I've wrote a interesting script here.")


f= open('message.txt', 'a+') # a+的作用是保留现有文件格式不变，在最末尾添加相关信息。
f.write("I have add another line here.\n")
f.close()