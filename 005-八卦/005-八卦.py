from turtle import *

title('八卦')

shape('turtle')
width(8)

def position(x,y):
    penup()
    setx(x)
    sety(y)
    pendown()

def eight_diagram(big_circle,small_circle):
    fillcolor('black')
    begin_fill()
    circle(big_circle,-180)
    circle(big_circle*2,180)
    circle(big_circle,180)
    position(0,big_circle+small_circle)
    circle(small_circle)
    end_fill()

    position(0,big_circle*2)
    circle(big_circle*2,-180)

    fillcolor('white')
    begin_fill()
    position(0,-(big_circle+small_circle))
    circle(small_circle)
    end_fill()

eight_diagram(132,44)

hideturtle()
done()
