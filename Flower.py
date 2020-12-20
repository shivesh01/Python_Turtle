import turtle as T
import random
T.bgcolor("black")
T.color ("white")
for i in range (20):
    x = random.randrange (-300,300)
    y = random.randrange (-300,300)
    rnd_range = random.randrange (10,90)
    T.penup()
    T.goto (x,y)
    T.pendown()
    for i in range (rnd_range):
        siz = random.randrange(5,16)
        T.forward(siz)
        T.back (siz)
        T.right (4)