# -*-coding:utf-8 -*-
import json

# user = input("请输入用户名：")
filename = 'users.txt'
with open(filename) as f_obj:
    content = json.load(f_obj)
    print(content)