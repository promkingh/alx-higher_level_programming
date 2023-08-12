#!/usr/bin/python3
for num1 in range(0, 100):
    if num1 == 99:
        print("{}{}".format(int(num1 / 10), num1 % 10))
    else:
        print("{}{}".format(int(num1 / 10), num1 % 10), end=', ')
