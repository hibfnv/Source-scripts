# -*-coding:utf-8 -*-
try:
    f = open('alice.txt', 'r')
    content = f.read()
    f.close()
    print(content)
except FileNotFoundError:
    print('Make sure the file was exist there, thanks.')
filename = 'talktome.txt'
f = open(filename, 'w')
f.write("This is a test content about talktome sentence.\n")
f.write("Hi Tom. How's going today?\n")
f.write("I'm fine. How about you?\n")
f.close()
with open(filename) as file_object:
    context = file_object.read()
    words = context.split()
    num_words = len(words)
print('\n')
print(context)
print("The file " + filename + "has about " + str(num_words) + " words.")