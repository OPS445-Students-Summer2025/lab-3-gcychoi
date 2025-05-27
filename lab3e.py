#!/usr/bin/env python3

# Name: lab3e.py
# Author: Chung Yin Choi
# Author ID: cychoi
# Date Created: 2025/05/25

my_list = [100, 200, 300, 'six hundred']

def give_list():
    return my_list[0:]

def give_first_item():
    return str(my_list[0])

def give_first_and_last_item():
    new_list = [my_list[0], my_list[-1]]
    return new_list

def give_second_and_third_item():
    return my_list[1:3]

if __name__ == '__main__':   # This section also referred to as a "main block"
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())


