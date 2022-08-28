import math
import turtle

l = turtle.Turtle()

l.color("black", "black")
l.speed(10)
l.getscreen().bgcolor("brown")
l.pensize(1)
l.shape("arrow")
for _ in range(5):

    for j in range(0, 5):

        l.begin_fill()
        for i in range(1, 26):

            l.forward(10)
            l.left(216)

            if i.__mod__(5) == 0:
               # l.penup()
                l.left(216)
                l.forward(20)
                l.pendown()
        l.end_fill()

        l.left(216)
        l.forward(200)
        l.pendown()

    l.left(216)
    l.forward(600)



turtle.done()