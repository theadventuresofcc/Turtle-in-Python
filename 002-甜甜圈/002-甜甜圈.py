from turtle import *

title('甜甜圈')

penup()
setx(0)
sety(58)
pendown()

shape('turtle')
width(2)
pencolor('#fcbabc')

for i in range(120):
    circle(99)
    right(3)
    forward(3)

hideturtle()
done()
