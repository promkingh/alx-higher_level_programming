#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = number % 10
if last_dig > 5:
    print(f"Last digit of {number} is {last_dig} and is greater than 5")
if last_dig == 0:
    
