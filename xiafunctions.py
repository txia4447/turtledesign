import turtle

bob=turtle.Turtle()
turtle.colormode(255)
bob.speed(0)

import turtle
bob=turtle.Turtle()
bob.speed(0)
turtle.colormode(255)

def mfirework(x,y):
    jump(x,y)
    fireworkm2(0.15)
    fireworkm(0.17)

def fireworkm2(distance):
    for times in range(18):
        curvelinem2(distance)
        bob.penup()
        rcurveline(distance)
        bob.pendown()
        bob.left(22.5)

def fireworkm(distance):
    for times in range(9):
        curvelinem(distance)
        bob.penup()
        rcurveline(distance)
        bob.pendown()
        bob.left(45)

def curvelinem2(distance):
    for times in range(40):
        c=255-times*4
        bob.color(255,c,255)
        bob.width(times*0.15)
        bob.forward(times *distance)
        bob.left(1)

def curvelinem(distance):
    for times in range(40):
        c=times*6
        bob.color(255,c,255)
        bob.width(times *0.15)
        bob.forward(times*distance)
        bob.left(1)


def cfirework(x,y):
    jump(x,y)
    fireworkc2(0.15)
    fireworkc(0.17)

def fireworkc2(distance):
    for times in range(18):
        curvelinec2(distance)
        bob.penup()
        rcurveline(distance)
        bob.pendown()
        bob.left(22.5)

def fireworkc(distance):
    for times in range(9):
        curvelinec(distance)
        bob.penup()
        rcurveline(distance)
        bob.pendown()
        bob.left(45)

def curvelinec2(distance):
    for times in range(40):
        c=255-times*4
        bob.color(c,255,255)
        bob.width(times*0.15)
        bob.forward(times *distance)
        bob.left(1)

def curvelinec(distance):
    for times in range(40):
        c=times*6
        bob.color(c,255,255)
        bob.width(times *0.15)
        bob.forward(times*distance)
        bob.left(1)


def gfirework(x,y):
    jump(x,y)
    fireworkg2(0.15)
    fireworkg(0.17)

def fireworkg2(distance):
    for times in range(18):
        curvelineg2(distance)
        bob.penup()
        rcurveline(distance)
        bob.pendown()
        bob.left(22.5)

def fireworkg(distance):
    for times in range(9):
        curvelineg(distance)
        bob.penup()
        rcurveline(distance)
        bob.pendown()
        bob.left(45)

def curvelineg2(distance):
    for times in range(40):
        c=255-times*4
        bob.color(c,255,c)
        bob.width(times*0.15)
        bob.forward(times *distance)
        bob.left(1)

def curvelineg(distance):
    for times in range(40):
        c=times*6
        bob.color(c,255,c)
        bob.width(times *0.15)
        bob.forward(times*distance)
        bob.left(1)

def rfirework(x,y):
    jump(x,y)
    fireworkr2(0.15)
    fireworkr(0.17)

def fireworkr2(distance):
    for times in range(18):
        curveliner2(distance)
        bob.penup()
        rcurveline(distance)
        bob.pendown()
        bob.left(22.5)

def fireworkr(distance):
    for times in range(9):
        curveliner(distance)
        bob.penup()
        rcurveline(distance)
        bob.pendown()
        bob.left(45)

def curveliner2(distance):
    for times in range(40):
        c=255-times*4
        bob.color(255,c,c)
        bob.width(times*0.15)
        bob.forward(times *distance)
        bob.left(1)

def curveliner(distance):
    for times in range(40):
        c=times*6
        bob.color(255,c,c)
        bob.width(times *0.15)
        bob.forward(times*distance)
        bob.left(1)

def bfirework(x,y):
    jump(x,y)
    fireworkb2(0.15)
    fireworkb(0.17)

def fireworkb2(distance):
    for times in range(18):
        curvelineb2(distance)
        bob.penup()
        rcurveline(distance)
        bob.pendown()
        bob.left(22.5)

def fireworkb(distance):
    for times in range(9):
        curvelineb(distance)
        bob.penup()
        rcurveline(distance)
        bob.pendown()
        bob.left(45)

def curvelineb2(distance):
    for times in range(40):
        c=255-times*4
        bob.color(c,c,255)
        bob.width(times*0.15)
        bob.forward(times *distance)
        bob.left(1)

def curvelineb(distance):
    for times in range(40):
        c=times*6
        bob.color(c,c,255)
        bob.width(times *0.15)
        bob.forward(times*distance)
        bob.left(1)


def yfirework(x,y):
    jump(x,y)
    firework2(0.15)
    firework(0.17)

def firework2(distance):
    for times in range(18):
        curveliney2(distance)
        bob.penup()
        rcurveline(distance)
        bob.pendown()
        bob.left(22.5)

def firework(distance):
    for times in range(9):
        curveliney(distance)
        bob.penup()
        rcurveline(distance)
        bob.pendown()
        bob.left(45)

def curveliney2(distance):
    for times in range(40):
        c=255-times*4
        bob.color(255,255,c)
        bob.width(times*0.15)
        bob.forward(times *distance)
        bob.left(1)

def curveliney(distance):
    for times in range(40):
        c=times*6
        bob.color(255,255,c)
        bob.width(times *0.15)
        bob.forward(times*distance)
        bob.left(1)

def rcurveline(distance):
    for times in range(40):
        c=234-times*6
        bob.color(255,255,c)
        bob.width(5.85-times *0.15)
        bob.backward(distance*39-times*distance)
        bob.right(1)
def fivecircle(color,distance):
    for times in range(5):
        bob.right(90)
        bob.begin_fill()
        bob.color(color)
        bob.circle(25)
        bob.end_fill()
        bob.left(90)
        bob.forward(100)
        bob.left(72)
        
def fireworks(distance):
    for times in range(16):
        curvelines(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(12+times*24)
        
def firework(distance):
    for times in range(16):
        curveline(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times*24)

def curvelines (distance):
    for times in range(40):
        c=255-times*4
        bob.color(255,255,c)
        bob.width(times *0.15)
        bob.forward(times *distance)
        bob.left(1)
        
def curveline (distance):
    for times in range(40):
        c=times*6
        bob.color(255,255,c)
        bob.width(times *0.15)
        bob.forward(times *distance)
        bob.left(1)
    
    
def spikeflower(distance):
    for times in range(11): 
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times*36)
        
def spike(distance):
    for times in range(20):
        c=times*12
        bob.color(c,c,c)
        bob.width(times*2)
        bob.forward(distance)
        bob.left(10)
    
def tile(c):
    polygon(4,200,c)
    for times in range(4):
        polygon(3,50,"black")
        bob.forward(50)
        polygon(3,50,"black")
        bob.forward(50)
        polygon(3,50,"black")
        bob.forward(50)
        polygon(3,50,"black")
        bob.forward(50)
        bob.left(90)

def rowtile(c):
    for times in range(4):
        tile(c)
        bob.forward(200)

def polygon(sides,distance,c):
    bob.color(c)
    angle=360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()
    
def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(distance,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(5):
        bob.forward(distance)
        bob.left(144)
    bob.end_fill()

def explosion(distance,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(8):
        bob.forward(distance)
        bob.left(135)
    bob.end_fill()

def figure1(distance,size,color):
    bob.begin_fill()
    bob.color(color)
    bob.circle(size)
    bob.forward(distance)
    bob.circle(size)
    bob.end_fill()
    bob.left(45)
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)
    bob.left(45)
    bob.begin_fill()
    bob.circle(size)
    bob.forward(distance)
    bob.circle(size)
    bob.end_fill()

def monster(color):
    bob.begin_fill()
    bob.color(color)
    bob.left(90)
    bob.forward(100)
    bob.left(180)
    bob.circle(50)
    bob.right(180)
    bob.right(90)
    bob.forward(100)
    bob.right(90)
    bob.forward(100)
    bob.right(150)
    bob.forward(50)
    bob.left(120)
    bob.forward(50)
    bob.right(120)
    bob.forward(50)
    bob.left(120)
    bob.forward(50)
    bob.end_fill()

def fadingtriangle():
    for times in range(50):
        c=(250-times*5,250-times*5,0)
        polygon(3,450-times*8,c)

def fadingstar():
    for times in range(100):
        c=(250-times*2,250-times*2,0)
        star(450-times*4,c)

def moon(x,y):
    jump(x,y)
    for times in range(1441):
        bob.color("yellow")
        cline(0.2)
        jump(x,y)
        bob.left(times *0.25)
        
def rcline(distance):
    for times in range(40):
        bob.backward(7.8-times*distance)
        bob.right(1)
        
def cline(distance):
    for times in range(40):
        bob.forward(times*distance)
        bob.left(1)




    
   
    
    
