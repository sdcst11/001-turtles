#!python3
"""
Python has some built in commands or functions.  Many of these functions will do a specific command and then generate a result.  One very useful function is called round(), and it rounds numbers to the appropriate decimal.

Functions all use the same format, they have a name and then 0 or more parameters.  If we were talking about Math, the parameters would be the input values that are used to generate an output.

Functions generally have a definition that includes, the name and what the input parameters might mean

round( number, decimals)
number is the float variable or value to be rounded
decimals is an optional parameter that specifes which decimal place to round to.  If it is not included, it rounds to the nearest whole number and results in an int type variable.  If the decimals value is included, then the result is a float type variable

Often, we don't just use the function, but we do something with the result.  
On line 22, we are storing the result into the variable x. Since x already had a value stored in it, we are updating or changing the value of x to store a new value instead.

On line 25, we are storing the result into a new variable y.  Usually, it does not matter if you choose to update an existing variable or create a new variable
Experiment with changing the values on lines 20 and 21.  You can add breakpoints on line 23 and 26 and track the values of the variables using the debugger.  Note on line 28 that we can also use numerical values directly as parameters, we don't have to use variables.
"""

x = 1.2222222222
numDecimals = 1
x = round(x , numDecimals)
print(x)

y = round(x)
print(y)

z = round(3.14159 , 2)
print(z)