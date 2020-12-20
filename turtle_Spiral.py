from turtle import *

bgcolor("black")
pensize(2)
pencolor('white')
speed(100)
for i in range(6):

    for color in ('red', 'magenta', 'blue', 'cyan', 'green', 'white', 'yellow'):
        pencolor(color)
        circle(70)
        left(10)
        hideturtle()


mainloop()

