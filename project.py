import turtle
turtle.bgcolor()
bob = turtle.Turtle()
tob = turtle.Turtle()
tob.speed(0)
tob.pensize(2)
for times in range(150):
    tob.pencolor('lightgreen')
    tob.circle(times*3)
    tob.rt(90)
   
    
bob.speed(0)
bob.begin_fill()
#going up
bob.pu()
bob.lt(90)
bob.fd(100)
bob.pd()

for times in range(90):
    bob.lt(0.5)
    bob.fd(2)

bob.lt(170)
"""---------------------------------------------------------------------"""
#first part going all the way down
for times in range(137):
    bob.rt(0.5)
    bob.fd(2)
"""---------------------------------------------------------------------"""
#making sides
bob.rt(112)
for times in range(60):
    bob.rt(0.6)
    bob.fd(3)

bob.lt(170)

for times in range(75):
    bob.lt(0.6)
    bob.fd(3)
"""---------------------------------------------------------------------"""
    
#done with leftside

bob.lt(99)
for times in range(90):
    bob.lt(0.5)
    bob.fd(2)

for times in range(88):
    bob.rt(0.5)
    bob.fd(2)
"""---------------------------------------------------------------------"""    
bob.rt(170)
#2nd part going all the way down
for times in range(147):
    bob.lt(0.5)
    bob.fd(2)
"""---------------------------------------------------------------------"""    
#making sides
bob.lt(112)
for times in range(60):
    bob.lt(0.6)
    bob.fd(3)

bob.rt(170)
for times in range(75):
    bob.rt(0.6)
    bob.fd(3)
"""---------------------------------------------------------------------"""
#done with rightside

bob.rt(98)
for times in range(90):
    bob.rt(0.5)
    bob.fd(2)

bob.end_fill()

bob.pu()
bob.rt(187)
bob.fd(80)
bob.left(180)
bob.fd(210)
bob.pd()
"""-------------------------------------------------------------------"""
#making an uperside
bob.begin_fill()
bob.left(180)
bob.rt(35)
for times in range(80):
    bob.rt(0.5)
    bob.fd(3)

bob.lt(168)
for times in range(70):
    bob.lt(0.5)
    bob.fd(3)


bob.rt(75)
for times in range(78):
    bob.lt(0.5)
    bob.fd(3)


bob.lt(168)
for times in range(87):
    bob.rt(0.5)
    bob.fd(3)

bob.end_fill()
"""--------------------------------------------------------------------"""
#uper sides
bob.pu()
bob.rt(121)
bob.forward(100)
bob.rt(88)
bob.fd(90)
bob.rt(115)
bob.fd(25)
bob.rt(2)
bob.pd()
bob.begin_fill()
bob.fd(12)
bob.rt(90)
for times in range(40):
    bob.rt(0.4)
    bob.fd(3)

bob.rt(170)

for times in range(40):
    bob.lt(0.4)
    bob.fd(3)
bob.end_fill()

bob.penup()
bob.rt(10)
bob.fd(54)
bob.rt(90)
bob.fd(23)
bob.pd()
bob.begin_fill()
bob.lt(110)
for imes in range(30):
    bob.lt(0.5)
    bob.fd(3)

bob.lt(121)
for imes in range(35):
    bob.lt(0.5)
    bob.fd(1.5)

bob.lt(110)
bob.fd(22)
bob.rt(90)
for times in range(10):
    bob.rt(0.5)
    bob.fd(3)
bob.end_fill()
bob.pu()
bob.lt(90)
bob.fd(200)
bob.rt(180)
bob.lt(45)
bob.fd(52)
bob.pd()

bob.begin_fill()
bob.lt(90)
for times in range(40):
    bob.lt(0.4)
    bob.fd(3)
bob.lt(170)

for times in range(40):
    bob.rt(0.4)
    bob.fd(3)
bob.end_fill()

bob.penup()
bob.lt(10)
bob.fd(54)
bob.lt(90)
bob.fd(5)
bob.pd()
bob.begin_fill()
bob.rt(127)
for imes in range(30):
    bob.rt(0.5)
    bob.fd(3)

bob.rt(121)
for imes in range(35):
    bob.rt(0.5)
    bob.fd(1.5)

bob.rt(110)
bob.fd(22)
bob.lt(90)
for times in range(10):
    bob.lt(0.5)
    bob.fd(3)
bob.end_fill()

bob.pu()
bob.rt(180)
bob.fd(150)
bob.lt(45)
bob.fd(10)
bob.rt(90)
bob.fd(35)
bob.rt(93)
bob.fd(70)
bob.rt(90)
bob.fd(30)
bob.rt(90)
bob.fd(10)
bob.rt(60)
bob.fd(5)
bob.pd()
bob.begin_fill()
for times in range(60):
    bob.lt(1)
    bob.fd(4)
bob.lt(172)
for times in range(46):
    bob.rt(1)
    bob.fd(4)
bob.end_fill()

bob.pu()
bob.rt(45)
bob.fd(300)
bob.rt(105)
bob.fd(200)
bob.rt(121)
bob.fd(150)
bob.rt(150)
bob.fd(12)
bob.pd()
bob.begin_fill()
bob.rt(105)
for times in range(55):
    bob.rt(1)
    bob.fd(4)
bob.rt(170)
for times in range(40):
    bob.lt(1)
    bob.fd(4)
bob.end_fill()

bob.pu()
bob.lt(90)
bob.fd(200)
bob.rt(186)
bob.fd(75)
bob.pd()
bob.begin_fill()
bob.fd(100)
bob.lt(120)
bob.fd(100)
bob.lt(120)
bob.fd(100)
bob.lt(120)
bob.end_fill()

bob.pu()
bob.fd(200)
bob.lt(90)
bob.fd(300)
bob.rt(90)
bob.pd()
bob.write('Yash')

turtle.done()

    
