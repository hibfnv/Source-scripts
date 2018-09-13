# -*- coding:utf-8 -*-
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print("Look!" + self.name + " has sit down now.")

    def rolling(self):
        print(self.name + " has rolled over.")


my_dog = Dog('Alice', 3)
print("This is my dog, he calls " + my_dog.name + ". He is " + str(my_dog.age) + " years old.")
print("The dog can do sit and roll action when you give him a signal.")
signal = input("Give the dog a command, 'sit' or 'roll'.")
if signal.lower() == 'sit' or signal.lower() == 's':
    my_dog.sit()
elif signal.lower() == 'roll' or signal.lower() == 'r':
    my_dog.rolling()
else:
    print("Sorry, " + my_dog.name + " can't understand what's that mean.")