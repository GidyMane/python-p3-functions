#!/usr/bin/env python3

def greet_programmer():
    print  ("Hello, programmer!") 
greet_programmer()   

def greet(name):
    print ("Hello, {}!".format(name))
def greet_with_default(name="programmer"):
    print ("Hello, {}!".format(name))

def add(num1, num2):
    return num1 + num2
add(97, 3)

def halve(number):
    return number / 2
halve(8)