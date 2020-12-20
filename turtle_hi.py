import turtle
frame = turtle.Screen().bgcolor("White")
draw = turtle.Turtle()

# The colour, width and speed of the pen is initialized
draw.color("Green")
draw.width(3)
draw.speed(10)

# Now lets get started with actual code
# printing letter H
draw.left(90)
draw.forward(70)
draw.penup()
draw.goto(0, 35)
draw.pendown()
draw.right(90)
draw.forward(30)
draw.penup()
draw.goto(30, 70)
draw.pendown()
draw.right(90)
draw.forward(70)


# printing I
draw.penup()
draw.goto(45, 0)
draw.pendown()
draw.left(90)
draw.forward(60)
draw.backward(30)
draw.left(90)
draw.forward(70)
draw.left(90)
draw.forward(30)
draw.left(180)
draw.forward(60)
draw.hideturtle()


turtle.mainloop()