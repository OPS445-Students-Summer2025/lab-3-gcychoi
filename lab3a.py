#!/usr/bin/env python3

# Name: lab3a.py
# Author: Chung Yin Choi
# Author ID: cychoi
# Date Created: 2025/05/25

# return_text_value() function

def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name 
    return greeting

# return_number_value() function

def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3



# Main Program



if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))




