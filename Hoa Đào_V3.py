import turtle
import random
from turtle import *
from time import sleep
# Drawing the trunk of the cherry blossom(60,t)
def tree(branchLen,t):
    sleep(0.0005)
    if branchLen >3:
        if 8<= branchLen <=12:
            if random.randint(0,2) == 0:
                t.color('snow') # white
            else:
                t.color('lightcoral') # Light coral
            t.pensize(branchLen / 3)
        elif branchLen <8:
            if random.randint(0,1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral') # Light coral
            t.pensize(branchLen / 2)
        else:
            t.color('sienna') # Ochre
            t.pensize(branchLen / 10) # 6
        t.forward(branchLen)
        a = 1.5 * random.random()
        t.right(20*a)
        b = 1.5 * random.random()
        tree(branchLen-10*b, t)
        t.left(40*a)
        tree(branchLen-10*b, t)
        t.right(20*a)
        t.up()
        t.backward(branchLen)
        t.down()
# Falling petals
def petal(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral') # Light coral
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)
def main():    
    # Drawing Area
    t = turtle.Turtle()
    # Canvas Size
    w = turtle.Screen()
    # Hide Brush
    t.hideturtle()
    getscreen().tracer(5,0)
    # wheat
    w.screensize(bg='wheat')
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color('sienna')
     # Drawing the trunk of the cherry blossom
    tree(60,t)
    # Falling petals
    petal(200, t)
    w.exitonclick()
main()