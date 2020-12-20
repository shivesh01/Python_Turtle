from turtle import *

color = ['red', 'orange', 'magenta', 'purple', 'blue', 'white', 'yellow', 'grey']
speed(10)
for value in range(200):
    pencolor(color[value % 8])
    width(value/200+1)
    forward(value)
    left(59)
mainloop()
