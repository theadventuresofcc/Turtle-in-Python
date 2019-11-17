from turtle import *

title('雪花')

shape('turtle')
width(12)
pencolor('white')
bgcolor('#00CED1')

def square():
    for i in range(4):
        forward(188)
        left(90)

for j in range(6):
    square()
    left(60)

hideturtle()
done()
