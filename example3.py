#!python3

import math

# The math module has many commands that you can import into Python
# Find out some of the math commands and built in constants at:
# https://docs.python.org/3/library/math.html
# https://www.w3schools.com/python/module_math.asp has a more user friendly display
# to use math commands, we use math.command()

print('This finds the value of a number rounded down')
print("---------------------------------------------")
num = 13.9
answer = math.floor(13.9)
print(f"{num} rounded down is {answer}")

# note the difference in syntax for the formatted string
# in the first example, we made a separate variable for it
# in the second example, we just evaluated the expression right in the string
print('This finds the value of a number rounded up')
print("---------------------------------------------")
num = 13.9
print(f"{num} rounded up is {math.ceil(num)}")
