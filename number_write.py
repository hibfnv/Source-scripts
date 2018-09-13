# -*-coding:utf-8 -*-
import json

numbers = [1, 3, 4, 5, 7, 9, 11, 15, 22]
filename = 'numbers.json'
f = open(filename, 'w')
json.dump(numbers,f)
f.close()
fn = open(filename, 'r')
numbers = json.load(fn)
print(numbers)
f.close()