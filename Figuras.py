import turtle
import tkinter as tk
import math

##plano
def plano(plano, esfera):
    plano.reset()
    esfera.reset()
    plano.width(3)
    plano.fillcolor("#ff6600")
    
    plano.penup()
    plano.goto(0,-100)
    plano.left(45)
    plano.pendown()
    plano.begin_fill()
    plano.back(150)
    plano.forward(300)
    plano.left(45)
    plano.forward(200)
    plano.right(45)
    plano.back(300)
    plano.left(45)
    plano.back(200)
    plano.end_fill()
    plano.penup()
    plano.goto(0,0)
    plano.goto(0,25)
    #plano.write("Densidad lineal:" + str(densidad) +"C/m")
    plano.goto(0,0)
    plano.pendown()
    plano.width(1)
    plano.goto(200,0)
    plano.hideturtle()
    plano.seth(0)

   
def fparticula(totald, part, color):

    part.color(str(color))
    part.shapesize(stretch_wid=0.25, stretch_len=0.25, outline=0.5)

    progress(float(totald), part)
    part.right(180)
    progress(float(totald), part)


def fparticulaesf(totald, part, color, radio):

    part.color(str(color))
    part.shapesize(stretch_wid=0.25, stretch_len=0.25, outline=0.5)

    if(totald > radio):
        progress(float(totald), part)
    
    else:
        progress(float(totald), part)
        part.right(180)
        progress(float(totald), part)


def progress(totald, tortuga):
    
    i = 0
    p = 0
    while(i < (totald-(totald/5))):
        i = i + (totald/20)
        if((p % 2) == 0):
            tortuga.forward(totald/5)
        else:
            tortuga.penup()
            tortuga.forward(totald/5)
            tortuga.pendown()
        p = p +1
    tortuga.forward(totald-i)



##Esfera

def esfera(part, plano):
    part.reset()
    plano.reset()
    val = 10

    for i in range(36):
        part.seth(-val)
        circle(part)
        val += 10

def circle(part):
    for i in range(2):
        part.speed(0)
        part.circle(100,90)
        part.circle(100//2,90)