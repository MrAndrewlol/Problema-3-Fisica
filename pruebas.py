import turtle
import tkinter as tk
from turtle import RawTurtle, ScrolledCanvas
import customtkinter as Ctk

#plano

def draw_grid(step, size,turtle):
    for i in range(-size, (size+1), step):
        turtle.penup()
        turtle.goto(i, -size)
        turtle.pendown()
        turtle.goto(i, size)
        
    for i in range(-size, (size+1), step):
        turtle.penup()
        turtle.goto(-size, i)
        turtle.pendown()
        turtle.goto(size, i)


def draw_grid(step, size,turtle):
    for i in range(-size, (size+1), step):
        turtle.penup()
        turtle.goto(i, -size)
        turtle.pendown()
        turtle.goto(i, size)
        
    for i in range(-size, (size+1), step):
        turtle.penup()
        turtle.goto(-size, i)
        turtle.pendown()
        turtle.goto(size, i)


def mainpos(tortuga,screensize):
    tortuga.penup()
    tortuga.goto(-screensize,0)
    tortuga.pendown()

def xbar(tortuga,screensize):
    tortuga.penup()
    tortuga.goto(-screensize,0)
    tortuga.pendown()
    tortuga.back(-screensize)
    tortuga.forward(screensize)
    tortuga.write("x+")
    tortuga.goto(0,0)

def ybar(tortuga,screensize):
    tortuga.penup()
    tortuga.goto(0,0)
    tortuga.pendown()
    tortuga.left(90)
    tortuga.backward(screensize-40)
    tortuga.forward((screensize-40)*2)
    tortuga.right(90)
    tortuga.write("y+")
    tortuga.goto(0,0)

def zbar(tortuga,screensize):
    tortuga.penup()
    tortuga.goto(0,0)
    tortuga.pendown()
    tortuga.left(30)
    tortuga.backward((screensize-90))
    tortuga.forward((screensize-90)*2)
    tortuga.right(30)
    tortuga.write("z+")
    tortuga.goto(0,0)

def pantalla(tortugagrid):
# Set up the screen
    tortugagrid._tracer(False)
    tortugagrid.color("#D3D3D3")
    screensize = 300
    actualscreen = 1000 #resolucion de la pantalla

    draw_grid(step=10, size = actualscreen, turtle=tortugagrid), 

    tortugagrid._tracer(True)
    tortugagrid.color("black")
    tortugagrid.shapesize(0.25,0.5,0.5)
    tortugagrid.speed(0)
    mainpos(tortugagrid,screensize)
    xbar(tortugagrid,screensize*1.9)
    ybar(tortugagrid,screensize*1.2)
    zbar(tortugagrid,screensize*1.5)

