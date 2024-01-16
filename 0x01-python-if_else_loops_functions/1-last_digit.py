#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number}", end = " ")
divide = number % 10
if number < 0 and divide != 0:
    print(f"is {(divide - 10)}", end " ")
else:
    print(f"is {divide}", end = " ")
if(number < 0 or divide < 6) and divide != 0:
    print("and is less than 6 and not 0")
elif divide > 5:
    print("and is greater than 5")
elif divide == 0:
    print("and is 0")
