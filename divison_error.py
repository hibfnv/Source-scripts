# -*-coding:utf-8 -*-
print("数学除法公式：")
x = input("请输入一个被数字：")
y = input("请输入一个除数: ")
try:
    if x.isdigit() and y.isdigit() and y != 0:
        print("x / y = ", int(x) / int(y))
except ZeroDivisionError:
    print("0不能做为除数，该等式不成立！")
# 利用while循环中使用异常来避免崩溃
print("使用while循环中的异常来避免崩溃。")
print("使用q或者quit来退出该脚本。")
while True:
    a = input("被除数：")
    if a == 'q' or a == 'quit':
        break
    b = input("除数：")
    try:
        result = int(a) / int(b)
        print("a / b = ", result)
    except ZeroDivisionError:
        print("除数不能为0,输入错误。")
    except ValueError:
        print("输入错误，请输入数值来进行运算。")
