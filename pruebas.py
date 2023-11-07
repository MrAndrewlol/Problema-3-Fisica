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
    tortuga.backward(screensize/2)
    tortuga.forward((screensize/2)*2)
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



def cilindro(tortuga, largo, diameter):
    radius = diameter/2
    tortuga.penup()
    tortuga.goto(-largo/2,-radius)
    tortuga.pendown()
    tortuga.forward(largo*2)

    tortuga.circle(radius)

    tortuga.setheading(90)
    tortuga.penup()
    tortuga.forward(2*radius)
    tortuga.pendown()
    tortuga.setheading(180)

    tortuga.forward(largo*2)

    tortuga.circle(radius, extent=180)  #  Draw 1/2 of the bottom/circle

    


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

def movelectron(tortuga, tortuga1, tortuga2,tortuga3, radio, largo, rapidez, tiempo, speed):
    contador = 0
    tortuga = tortuga1 = tortuga2 = tortuga3
    while(contador  < tiempo):
        if(rapidez >=0):
            tortuga.penup()
            tortuga.showturtle()
            tortuga.speed(speed)
            tortuga.goto(-largo/2, radio/2)
            tortuga.forward(largo)
            tortuga.hideturtle()
            tortuga.back(largo)
        if(rapidez <=0):
            tortuga.showturtle()
            tortuga.speed(speed)
            tortuga.penup()
            tortuga.goto(-largo/2, radio)
            tortuga.forward(largo)
            tortuga.forward(largo)
            tortuga.back(largo)
        contador = contador +1
        

# app = tk.Tk()  # create CTk window like you do with the Tk window
# app.geometry("1530x1080+0+0") #1920 -1080
# canvas = tk.Canvas(app) ##Cambiar la resolucion de la pantalla de la tortuga
# canvas.pack()

# screen = turtle.TurtleScreen(canvas)
# canvas.config(width=2000, height=1080)
# tortugagrid = RawTurtle(screen) 
# tortucil = RawTurtle(screen) 
# pantalla(tortugagrid)
# cilindro(tortucil,500,100)
# tortu1 = RawTurtle(screen, shape="circle")
# tortu1.color("blue") 
# tortu2 = RawTurtle(screen) 
# tortu3 = RawTurtle(screen) 
# tortu4 = RawTurtle(screen) 
# movelectron(tortu1,tortu2, tortu3,tortu4 ,100/4, 500, 12, 2,1)



    

#app.mainloop()

