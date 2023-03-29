import turtle
from turtle import *
import time
#Screen settings
screen = turtle.Screen()
screen.title("How to Draw Kirby")
screen.setup(width=500, height=500)

#Color
classicRose = "#FFC1E7"
darkPink = "#FFB3E1"
Rose  = "#f871ab"
Desert = '#FFD99D'

#Turtles
kirbyBody = turtle.Turtle()
kirbyBodyColor = turtle.Turtle()
kirbyLtEye = turtle.Turtle()
kirbyRtEye = turtle.Turtle()
kirbyMouth = turtle.Turtle()
kirbyLtArm =turtle.Turtle()
kirbyRtArm =turtle.Turtle()
kirbyLtLeg =turtle.Turtle()
kirbyRtLeg =turtle.Turtle()
kirbyText = turtle.Turtle()
st = turtle.Turtle()

#Star Shape
st.hideturtle()
st.pu()
st.speed(10)
st.begin_poly() 
for i in range(5):
    st.fd(100)
    st.rt(144)
pairs = st.get_poly() 
turtle.register_shape("star", pairs)
st.fillcolor(Desert)
st.clear()

#Lists
v_list = [kirbyLtEye, kirbyRtEye, kirbyBody, kirbyMouth, kirbyLtArm, kirbyRtArm, kirbyLtLeg, kirbyRtLeg]
for v in v_list:
    v.pu()
    v.hideturtle()
    v.speed(10)
    v.pencolor("black")
    v.pensize(4)
    v.shape("star") 
    v.shapesize(0.275)
    v.fillcolor(Desert)

s_list = [kirbyLtEye, kirbyRtEye]
for s in s_list:
    s.speed(0)

d_list = [kirbyBodyColor, kirbyText]
for d in d_list:
    d.hideturtle()
    d.pu()
    d.speed(0)

# def section
def body(color, color2):
    kirbyBody.pd()
    kirbyBody.showturtle()
    kirbyBody.begin_fill()
    kirbyBody.circle(90)
    kirbyBody.fillcolor(color)
    kirbyBody.end_fill()
    kirbyLtArm.fillcolor(Desert)
    kirbyBody.pu()
    kirbyBody.hideturtle()
    kirbyBody.goto(0, 63)
    kirbyBody.dot(150, color2)

def cheekshade(rad, color):
    for i in range(2):
        kirbyBodyColor.hideturtle()
        kirbyBodyColor.fillcolor(color)
        kirbyBodyColor.begin_fill()
        kirbyBodyColor.circle(rad,75)
        kirbyBodyColor.circle(rad//4,105)
        kirbyBodyColor.end_fill()

def eye(rad):
    for i in range(2):
        kirbyRtEye.circle(rad,75)
        kirbyRtEye.circle(rad//4,105)
        kirbyLtEye.circle(rad,75)
        kirbyLtEye.circle(rad//4,105)

def mouth(color):
    kirbyMouth.pd()
    kirbyMouth.lt(270)
    kirbyMouth.showturtle()
    kirbyMouth.begin_fill()
    kirbyMouth.circle(20,180)
    kirbyMouth.setx(-20)
    kirbyMouth.fillcolor(color)
    kirbyMouth.end_fill()
    kirbyMouth.fillcolor(Desert)

def RtArm(color):
    kirbyRtArm.pd()
    kirbyRtArm.lt(35)
    kirbyRtArm.showturtle()
    kirbyRtArm.begin_fill()
    kirbyRtArm.circle(37,180)
    kirbyRtArm.fillcolor(color)
    kirbyRtArm.end_fill()
    kirbyRtArm.fillcolor(Desert)

def LtArm(rad, color):
    kirbyLtArm.pd()
    kirbyLtArm.lt(205)
    kirbyLtArm.showturtle()
    kirbyLtArm.begin_fill()
    kirbyLtArm.circle(rad,65)
    kirbyLtArm.circle(rad//2,105)
    kirbyLtArm.fillcolor(color)
    kirbyLtArm.end_fill()
    kirbyLtArm.fillcolor(Desert)

def LtLeg(rad, color):
    kirbyLtLeg.pd()
    kirbyLtLeg.lt(275)
    kirbyLtLeg.showturtle()
    kirbyLtLeg.begin_fill()
    for i in range(2):
        kirbyLtLeg.circle(rad,75)
        kirbyLtLeg.circle(rad//4,105)
    kirbyLtLeg.fillcolor(color)
    kirbyLtLeg.end_fill()
    kirbyLtLeg.fillcolor(Desert)
    
def RtLeg(rad, color):
    kirbyRtLeg.pd()
    kirbyRtLeg.lt(325)
    kirbyRtLeg.showturtle()
    kirbyRtLeg.begin_fill()
    for i in range(2):
        kirbyRtLeg.circle(rad,75)
        kirbyRtLeg.circle(rad//4,105)
    kirbyRtLeg.fillcolor(color)
    kirbyRtLeg.end_fill()
    kirbyRtLeg.fillcolor(Desert)

#RtLeg
kirbyRtLeg.goto(15,-40)
RtLeg(60, Rose)
kirbyRtLeg.hideturtle()

#Body
kirbyBody.goto(0, -40)
kirbyBody.seth(0)
kirbyLtArm.fillcolor(Desert)
body(darkPink, classicRose)

#Cheek    
kirbyBodyColor.goto(60, 60)
kirbyBodyColor.lt(143)
kirbyBodyColor.goto(60,60)
cheekshade(20, Rose)
kirbyBodyColor.goto(-40, 60)
cheekshade(20, Rose)

#Eyes
kirbyRtEye.goto(25, 75)
kirbyLtEye.goto(-15, 75)
kirbyRtEye.lt(58)
kirbyLtEye.lt(42)
for s in s_list:
    s.pd()
    s.begin_fill()
    s.showturtle()
eye(25)
for s in s_list:
    s.fillcolor('black')
    s.end_fill()
    s.fillcolor(Desert)
kirbyRtEye.goto(18,97)
kirbyRtEye.dot(15, 'white')
kirbyLtEye.goto(-16,97)
kirbyLtEye.dot(15, 'white')
time.sleep(0.3)
kirbyLtEye.hideturtle()
kirbyRtEye.hideturtle()

#Mouth
kirbyMouth.speed(0)
kirbyMouth.goto(-20,60)
mouth(Rose)
time.sleep(0.3)
kirbyMouth.hideturtle()

#RightArm
kirbyRtArm.goto(90,68)
RtArm(darkPink)
time.sleep(0.3)
kirbyRtArm.hideturtle()

#LeftArm
kirbyLtArm.goto(-88,71)
LtArm(50, darkPink)
time.sleep(0.3)
kirbyLtArm.hideturtle()

#LeftLeg
kirbyLtLeg.goto(-95,10)
LtLeg(60, Rose)
kirbyLtLeg.hideturtle()

turtle.mainloop()