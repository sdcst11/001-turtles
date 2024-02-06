## SDSS Computing Studies Python Assignment
### Basic Code in Python with Turtle Graphics

Objectives:
* To become familiar with the terminal
* To not get too scared when you see a github page
* To see the Python interpreter in action and exit it when necessary

Introduction
We will start by seeing how we can make some basic programming instructions using the Python interpeter.  You can do much of your work in the terminal.

1. Open the Visual Studio Code Program
2. Open a new terminal in Visual Studio Code.  You can do this from the main menu using the menu options: 
```
Terminal > New Terminal
```
3. The terminal is a command line environment.  You can see a "prompt" waiting for you to input a command.  Instead of a Graphical User Interface, everything is typed into the command line.  There are many commands for doing things like navigating around your computer, or viewing the contents of the local directory, or even modifying, deleting or copying files.  Sounds tedious, but there are some shortcuts!  Common ones:
```
    a. Up/Down Arrows: scrolls through previous commands
    b. Tab - autocompletion
```
4. On a Windows computer, type in 
```
py
```  
On a Mac/Linux computer, type in
```
python3
```
this will start a python session. You will recognize it by the prompt (where you type in commands) turning into a 
```
>>>
```
5. Type 
```
exit()
```  
Note that his is how you can exit from a python session. This is important because when we normally run programs from VSC, it will start a python session, and if one is open, it can't open another.  Knowing how to close a python session with exit() can be helpful
6. Re-enter a python session and type in the following commands:
```
import turtle
s = turtle.getscreen()
```

7. You may not notice it, but another window has opened up. It will look like this:
![Turtle Graphics Image](turtlescreen.png)
8. Let's create a turtle we can control using:
```
t = turtle.Turtle()
t.forward(100)
```
9. The new turtle moves forward 100 pixels, dragging a pen behind it as it goes. Some of the other commands that you can use to move the turtle around include:

```
t.right(<degrees>)
t.left(<degrees>)
These turn your turtle left or right the number of degrees you specify. Example: t.right(90)
```
```
t.forward(<distance>)
t.backward(<distance>)
These are measured in pixels (short for pixel elements).  Each pixel is a single dot on your screen. Very tiny.  Example: t.forward(20)
```
```
t.penup()
t.pendown()

This picks up or puts the pen down to allow the turtle to draw while it moves
```
```
t.speed(<speed>)
Makes your turtle move faster.  Speed should be a number. Example: t.speed(4)
```
```
t.pencolor(<color>)
Changes the color of the line.  It should be a color in quotation marks. Example: t.pencolor("red")
```
```
t.setheading(<angle>)
Sets the heading of the turtle to a specific degrees (0 is east, and increases counterclockwise.
Example: t.setheading(0)
```

10. Typing in your commands one at a time can be very tedious, so we can add the commands to a file.  Create a new file from the main menu using commands File > New Text File.  Type the following into the window.  The commands should look familiar!
```
import turtle

s = turtle.getscreen()
```
11. You will need to now safe the file with the correct file extension so that the computer knows it is a python program file.  Choose the menu options File > Save As and call the program "drawing.py" (almost anything as long as it has the .py extension at the end.)
11. Run the program using the Menu Options Run > Start Debugging (note the hotkey option!)  You may need to follow the prompts to install a python debugger.  Alternatively, you can also click on the little play symbol in the top right of the window. It looks like this: ![Play Icon](play.png)
12. You will notice that the program blips in and disappears very quickly.  That's because computers are fast. It is running the program, and when it is complete, it disappears.  We will introduce a pause into the program using the following command at the end of your program:
```
input()
```
13. Your program should look something like the contents of the file: 01.drawing.py
14. Create a drawing using only the command included in this file.  Remember that your turtle will always start facing east in the middle of the screen, and you may want to penup and move to a new location before you start drawing.

All finished? 
Read through the document at https://realpython.com/beginners-guide-python-turtle/ and experiment with the turtle.
