import turtle
import tkinter as tk
from turtle import RawTurtle, ScrolledCanvas
import customtkinter as Ctk

def mainpos(tortuga,screensize):
    tortuga.penup()
    tortuga.goto(-screensize,0)
    tortuga.pendown()

def cilindro(tortuga, largo = 1000, diameter = 50):
    tortuga._tracer(0)
    radius = diameter/2
    tortuga.forward(largo/2)
    tortuga.circle(radius)
    tortuga.setheading(90)
    tortuga.penup()
    tortuga.forward(2*radius)
    tortuga.pendown()
    tortuga.setheading(180)
    tortuga.forward(largo)
    tortuga.circle(radius, extent=180) #  Draw 1/2 of the bottom/circle
    tortuga.forward(largo/2)

    


def pantalla(tortugagrid):
# Set up the screen
    tortugagrid._tracer(False)
    tortugagrid.color("#D3D3D3")
    screensize = 300
    actualscreen = 1000 #resolucion de la pantalla

    tortugagrid._tracer(True)
    tortugagrid.color("black")
    tortugagrid.shapesize(0.25,0.5,0.5)
    tortugagrid.speed(0)
    mainpos(tortugagrid,screensize)

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
        
#Draw battery
def drawBattery(tortuga):
    tortuga._tracer(0)
    tortuga.penup()
    tortuga.goto(-3,-150)
    tortuga.pendown()
    tortuga.left(90)
    tortuga.forward(50)
    tortuga.backward(100)
    tortuga.penup()
    tortuga.goto(-6,-95)
    tortuga.pendown()
    tortuga.write("+", font = ("Arial",16,"normal"))
    tortuga.penup()
    tortuga.goto(3,-150)
    tortuga.pendown()
    tortuga.forward(25)
    tortuga.backward(50)
    tortuga.penup()
    tortuga.goto(3,-120)
    tortuga.pendown()
    tortuga.write("-", font = ("Arial",16,"normal"))
    tortuga.penup()
    tortuga.goto(0,0)
    tortuga.pendown()
    tortuga.setheading(0)

def drawCable(tortuga):
    tortuga._tracer(0)
    #Cable 1
    tortuga.penup()
    tortuga.goto(500,25)
    tortuga.setheading(0)
    tortuga.pendown()
    tortuga.forward(50)
    tortuga.setheading(270)
    tortuga.goto(550,-150)
    tortuga.setheading(180)
    tortuga.goto(3,-150)

    tortuga.penup()
    tortuga.goto(-525,25)
    tortuga.pendown()
    tortuga.setheading(180)

    #Cable 2
    tortuga.forward(25)
    tortuga.setheading(270)
    tortuga.goto(-550,-150)
    tortuga.setheading(0)
    tortuga.goto(-3,-150)

def drawLentgh(tortuga, length, prefijo):
    if prefijo == "--":
        prefijo = ""
    tortuga.color("red")
    tortuga.penup()
    tortuga.goto(-500,100)
    tortuga.pendown()
    tortuga.setheading(90)
    tortuga.forward(15)
    tortuga.backward(30)
    tortuga.forward(15)
    tortuga.setheading(0)
    tortuga.goto(500,100)
    tortuga.setheading(90)
    tortuga.forward(15)
    tortuga.backward(30)
    tortuga.forward(15)
    tortuga.setheading(0)
    tortuga.penup()
    tortuga.goto(0,125)
    tortuga.pendown()
    tortuga.write("largo = " + length + " " + prefijo + "m", font = ("Arial",16,"normal"))

    

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



    

# app.mainloop()

