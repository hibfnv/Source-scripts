# -*-coding:utf-8 -*-
# 导入json模块
import json

# 获取用户输入信息
username = input("用户名：")
filename = 'users.json'
f = open(filename, 'w')
json.dump(username, f)
print('Hi ' + username + '.欢迎来到python的世界.\n')
f.close()
# 使用json加载模块对文件进行加载。
print("对文件进行加载查看操作，并打印出用户信息。\n")
fn = open(filename, 'r')
user = json.load(fn)
print("Hi " + user +"!欢迎回来，这是我们第二次见面了。")
f.close()