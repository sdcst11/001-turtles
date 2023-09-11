## SDSS Computing Studies Python Assignment
### Basic Code in Python with Turtle Graphics

Objectives:
* To become familiar with the terminal
* To see the Python interpreter in action and exit it when necessary

Introduction
We will start by seeing how we can make some basic programming instructions using the Python interpeter.  You can do much of your work in the terminal.

1. Right click on the tab that this file is in, and choose the "Open Preview" option. Note that this will open up this file in another tab, but with important formatting changes.
2. Open a new terminal in Visual Studio Code
3. Type in "py"  this will start a python session. You will recognize it by the prompt (where you type in commands) turning into a >>>
4. Type exit()  Note that his is how you can exit from a python session. This is important because when we normally run programs from VSC, it will start a python session, and if one is open, it can't open another.  Knowing how to close a python session with exit() can be helpful
5. Re-enter a python session and type in the following commands:
```
import turtle
s = turtle.getscreen()
```
6. A window opens up with a turtle that we can control.
7. Let's create a turtle we can control using:
```
t = turtle.Turtle()
t.forward(100)
```
8. The new turtle moves forward 100 pixels, dragging a pen behind it as it goes.
9. Read through the document at https://realpython.com/beginners-guide-python-turtle/ and experiment with the turtle.
10. Tomorrow, we will use the information in this document to draw a picture using the turtle!