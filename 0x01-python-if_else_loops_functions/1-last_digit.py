#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
print(f"Last digit of {number} is", end="")
if number < 0:
    if last_digit == 0:
        print(f" {-last_digit} and is 0")
    else:
        print(f" {-last_digit} and is less than 6 and not 0")
else:
    if last_digit == 0:
        print(f" {last_digit} and is 0")
    elif last_digit > 5:
        print(f" {last_digit} and is greater than 5")
    else:
        print(f" {last_digit} and is less than 6 and not 0")
