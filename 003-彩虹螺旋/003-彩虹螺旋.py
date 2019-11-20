from turtle import *

title('彩虹螺旋')

shape('turtle')
width(2)
bgcolor('black')

colors=['red','orange','yellow','green','blue','indigo','violet']

for i in range(246):
    pencolor(colors[i%7])
    forward(i)
    left(51)
    
hideturtle()
done()
