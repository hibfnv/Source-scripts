print("Read line function used for the script.")
filename = "pi_digit.txt"
with open(filename) as file_object:
    for line in file_object:
        """未进行右边空白符号裁剪的情况下"""
        print(line)
print('\n')
print('This is second function about readlines.')
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for ln in lines:
    pi_string += ln.rstrip()
print(pi_string)
print("The total characters is ", len(pi_string))
print('\n')
# 这是一个空的注释行
# 对右边的空白符进行了裁剪
print("Use right strip function to cut blank space.")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
print('\n')
print("Cut the blank space at the beginning and the end.")
pi_string1 = ''
with open(filename) as file_object:
    for ln2 in lines:
        pi_string1 += ln2.strip()
print(pi_string1)
print("The total characters is ", len(pi_string1))