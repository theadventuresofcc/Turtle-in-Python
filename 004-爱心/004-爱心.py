from turtle import *

title('爱心')

penup()
setx(0)
sety(-234)
pendown()

shape('turtle')
width(18)
pencolor('#3f3f3f')
fillcolor('red')

begin_fill()
left(45)
forward(300)
circle(150,180)
right(90)
circle(150,180)
forward(300)
end_fill()

hideturtle()
done()
