# coding:utf-8
import turtle as t
import time

t.pensize(4)
t.color('blue')
t.hideturtle()
t.setup(800,600)
t.speed(0)


t.penup()
t.goto(200,50)
t.color('black','blue')
t.fillcolor('blue')
t.pendown()
t.seth(30)
t.circle(100,360)


t.penup()
t.goto(120,210)
t.pendown()
t.seth(180)
a=0.4
for i in range(120):
    if 0<=i<30 or 60<=i<90:
        a=a+0.05
        t.lt(3) 
        t.fd(a) 
    else:
        a=a-0.05
        t.lt(3)
        t.fd(a)

t.pu()
t.seth(-70)
t.fd(17)
t.seth(180)
t.pd()
t.begin_fill()
a=0.15
for i in range(120):
    if 0<=i<30 or 60<=i<90:
        a=a+0.02
        t.lt(3) 
        t.fd(a) 
    else:
        a=a-0.02
        t.lt(3)
        t.fd(a)
t.color('black')
t.end_fill()

t.pu()
t.seth(-90)
t.fd(5)
t.pd()
t.color('white')
t.begin_fill()
t.circle(2)
t.end_fill()


t.pu()
t.goto(180,210)
t.pencolor('black')
t.pd()
t.seth(180)
a=0.4
for i in range(120):
    if 0<=i<30 or 60<=i<90:
        a=a+0.05
        t.lt(3) 
        t.fd(a) 
    else:
        a=a-0.05
        t.lt(3)
        t.fd(a)

t.pu()
t.seth(-110)
t.fd(17)
t.seth(180)
t.pd()
t.begin_fill()
a=0.15
for i in range(120):
    if 0<=i<30 or 60<=i<90:
        a=a+0.02
        t.lt(3) 
        t.fd(a) 
    else:
        a=a-0.02
        t.lt(3)
        t.fd(a)
t.color('black')
t.end_fill()

t.pu()
t.seth(-90)
t.fd(5)
t.pd()
t.color('white')
t.begin_fill()
t.circle(2)
t.end_fill()


t.pu()
t.color('black','red') 
t.goto(150,160)
t.seth(180)
t.pd()
t.begin_fill()
t.circle(10)
t.end_fill()

t.pu()
t.seth(-90)
t.fd(5)
t.pd()
t.color('white')
t.begin_fill()
t.circle(2)
t.end_fill()


t.pu()
t.pencolor('black')
t.seth(-90)
t.fd(12)
t.pd()
t.fd(70)

t.pu()
t.seth(90)
t.fd(17)
t.seth(0)
t.fd(-60)
t.pd()
t.seth(-50)
t.circle(80,100)


t.penup()
t.goto(190,50)
t.color('black','blue')
t.fillcolor('blue')
t.pendown()
t.seth(30)
t.circle(80,360)
 

t.pu()
t.goto(200,150)
t.seth(30)
t.pd()
t.fd(30)

t.pu()
t.seth(180)
t.fd(23)
t.seth(-90)
t.fd(25)
t.pd()
t.seth(10)
t.fd(30)

t.pu()
t.seth(180)
t.fd(28)
t.seth(-90)
t.fd(20)
t.pd()
t.seth(-10)
t.fd(30)

t.pu()
t.goto(100,150)
t.seth(150)
t.pd()
t.fd(30)

t.pu()
t.seth(0)
t.fd(23)
t.seth(-90)
t.fd(25)
t.pd()
t.seth(170)
t.fd(30)

t.pu()
t.seth(0)
t.fd(28)
t.seth(-90)
t.fd(20)
t.pd()
t.seth(-170)
t.fd(30)

t.done()
time.sleep(1)
