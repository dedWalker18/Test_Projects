import turtle
from turtle import *

l = turtle.Turtle()
l.speed(500)
l.color("red", "yellow")
l.shape("circle")
l.begin_fill()
l.penup()
l.forward(50)
l.pendown()
l.left(10)
for i in range(432):
    l.forward(100)
    l.left(170)
    l.forward(100)
    l.right(170)
    l.forward(100)
    l.left(170)
    if i.__mod__(36) == 0:
        l.penup()
        l.forward(400)
        l.pendown()
        l.left(150)


l.end_fill()






turtle.done()