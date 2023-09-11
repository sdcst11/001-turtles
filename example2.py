#!python3

'''
Sometimes we want to make use of commands that are not part of the regular, basic Python set.  They are stored in external files called 'packages' or 'modules'.  You can think of these as expansion packs, like you might buy for a game.

An important and useful module is the math module.  In this file, you will see how we can import the module and use it's commands

The first thing we do is use the import command.  This always should be placed at the top of your file, before any of your commands
'''

import math

'''
To see what commands we can use from the math module, visit
https://docs.python.org/3/library/math.html
or
https://www.w3schools.com/python/module_math.asp

the math module has some commands (functions) and some constants (values)

Some useful commands include:
math.pow( x , y ) - returns the value of x to the power of y. 
This is the same as doing x**y

math.sqrt( x ) - determines the value of the square root of x
This is the same as doing x**0.5 (remember that a square root is the same as a power of 1/2)

Note that when using a command from the math module, you must include the prefix math followed by a period
'''

x = 4
a = math.pow(x,2)
print(a)

b = math.sqrt(x)
print(b)


