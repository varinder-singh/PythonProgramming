# This program is to explain how generators are effiecient to use as compared to other data structures in python

import sys


def my_range(n: int):
    print("My_range is called just now")
    start = 0
    while start < n:
        print("yielding the result from here")
        yield start
        start = start + 1


big_list = []

big_range = my_range(5)

for value in big_range:
    big_list.append(value)


print(big_list)
print(big_range)
