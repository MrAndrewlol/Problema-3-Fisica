import turtle
from turtle import RawTurtle, ScrolledCanvas
import tkinter as tk
import Figuras as figure
import Funciones as func

class esfera:
    def __init__(self, radio, carga, cargaparticula, masa, rapidez):
        self.radio = radio
        self.carga = carga
        self.masa = masa
        self.cargaparticula = cargaparticula
        self.rapidez = rapidez


class plano:
    def __init__(self, densidad,cargaparticula, masa, rapidez):
        self.densidad = densidad
        self.masa = masa
        self.cargaparticula = cargaparticula
        self.rapidez = rapidez

def eliminarrecorrido(tortu):
    tortu.clear()

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
    tortuga.left(45)
    tortuga.backward((screensize-90))
    tortuga.forward((screensize-90)*2)
    tortuga.right(45)
    tortuga.write("z+")
    tortuga.goto(0,0)

def dot(size,t):
    t.color("red")
    t.dot(size)

#plano

def pantalla():
    # Set up the screen
    tortugagrid = turtle.RawTurtle(screen, shape="arrow")
    tortugagrid._tracer(False)
    tortugagrid.color("#D3D3D3")
    screensize = 300
    actualscreen = 800 #resolucion de la pantalla

    draw_grid(step=10, size = actualscreen, turtle=tortugagrid), 

    tortugagrid._tracer(True)
    tortugagrid.color("black")
    tortugagrid.shapesize(0.25,0.5,0.5)
    tortugagrid.speed(0)
    mainpos(tortugagrid,screensize)
    xbar(tortugagrid,screensize)
    ybar(tortugagrid,screensize)
    zbar(tortugagrid,screensize)

def seleccionar_elementos(elegido):
    if elegido == "Personalizado":
        charge.grid(row=23,column=0)
        entrycargapart.grid(row=24, column=0)
        massLabel.grid(row=25,column=0)
        masa.grid(row=26,column=0)

    else :
        charge.grid_remove()
        entrycargapart.grid_remove()
        massLabel.grid_remove()
        masa.grid_remove()

def check_button_command(entrycargaesfera):
    
    if (eleccion.get() == 1):
        datos.config(text="Se selecciono la esfera")
        dato1.config(text="Escribir el radio (m)")
        dato1.grid(row=5,column=0)
        entryradio.grid(row=6,column=0)
        dato2.config(text="Escribir la carga negativa (C)")
        dato2.grid(row=7,column=0)
        entrycargaesfera.grid(row=8,column=0)
        figure.esfera(esferas, planos)
        
        


    if (eleccion.get() == 2):
        
        dato2.grid_remove()
        entrycargaesfera.grid_remove()
        entryradio.grid_remove()
        datos.config(text="Se selecciono el plano infinito")
        dato1.config(text="Escribir la densidad superficial de carga (C/m^2)")
        dato1.grid(row=5,column=0)
        entrydens.grid(row=6,column=0)
        figure.plano( planos, esferas)
    
    if (eleccion.get() == 0 ):
        datos.config(text="Esperando la selección de la carga central....")
        dato1.grid_remove()
        dato2.grid_remove()
        entrycargaesfera.grid_remove()
        entryradio.grid_remove()
        entrydens.grid_remove()

        

def meterdatos(cond, carga,masa,rapidez, radio,cargaesfera,densidad, particula, eleccion, tortu):
    if masa == '':
        masa = 0
    tortu.hideturtle()
    tortu.clear()
    tortu.hideturtle()
    tortu.color(dicColors[particula])
    #plane
    if eleccion == 2:
        errur.config(text="", bg="white")
        veloEscape.grid_remove()
        if(float(densidad) < 0):

            if float(rapidez) > 300000000:
                velo.config(text=f"Rapidez inicial -> ERROR: Velocidad de la luz superada")
                dist.config(text=f"Distancia recorrida: INFINITA")

            else :
                if particula == "Personalizado":
                    distance = func.distancePP(rapidez, densidad, masa, carga)
                    velo.config(text=f"Rapidez inicial: {rapidez} m/s")
                    dist.config(text=f"Distancia recorrida: {distance} m")
                    decimals = func.decimals(distance)
                    tortu.heading()
                    tortu.forward(distance*10**(decimals))      
                else:
                    distance = func.distanceP(rapidez, densidad, dicprotones[nombrepart], dicneutrones[nombrepart], nombrepart)
                    velo.config(text=f"Rapidez inicial: {rapidez} m/s")
                    dist.config(text=f"Distancia recorrida: {distance} m")
                    decimals = func.decimals(distance)
                    tortu.heading()
                    tortu.forward(distance*10**(decimals))
        else:
            errur.config(text="ERROR: Densidad lineal debe ser negativo", bg="red")
    
    #sphere
    elif eleccion == 1:
        errur.config(text="", bg="white")
        veloEscape.grid(row=44,column=1)
        tortu.penup()
        tortu.goto(160,0)
        tortu.pendown()
        if(float(cargaesfera) < 0):
                
            if float(rapidez) > 300000000:
                velo.config(text=f"Rapidez inicial: ERROR -> Velocidad de la luz superada por lo tanto es un agujero negro")
                dist.config(text=f"Distancia recorrida: INFINITA")

            else :
                veloEscape.config(text=f"Velocidad de escape: {func.escapeV(float(masa),float(cargaesfera),float(radio),nombrepart, dicprotones[nombrepart],dicneutrones[nombrepart])} m/s")
                if nombrepart == "Personalizado":
                    distance = func.distanceSP(radio, masa, rapidez, carga, cargaesfera)
                    velo.config(text=f"Rapidez inicial: {rapidez} m/s")
                    if (float(rapidez) > func.escapeV(float(masa),1.6**10-19,float(cargaesfera),float(radio),particula)):
                        dist.config(text=f"Distancia recorrida: INFINITA")
                    else:
                        dist.config(text=f"Distancia recorrida: {distance} m")
                        decimals = func.decimals(distance-1)
                        tortu.heading()
                        tortu.forward(distance*10**(decimals))      
                else:
                    distance = func.distanceS(radio, dicprotones[particula], dicneutrones[particula], rapidez, particula, cargaesfera)
                    velo.config(text=f"Rapidez inicial: {rapidez} m/s")
                    if (float(rapidez) > func.escapeV(float(masa),float(cargaesfera),float(radio),particula,dicprotones[particula], dicneutrones[particula])):
                        dist.config(text=f"Distancia recorrida: INFINITA")
                    else:
                        dist.config(text=f"Distancia recorrida: {distance} m")
                    decimals = func.decimals(distance)
                    tortu.heading()
                    tortu.forward(distance*10**(decimals-1))
        else:
            errur.config(text="ERROR: La carga de la esfera debese ser Negativa", bg="red")



if __name__ == "__main__":

    global cesfera
    cesfera = esfera(radio=1, carga=1, cargaparticula=1, masa=1, rapidez=1)
    global cplano
    cplano = plano(densidad= 1, cargaparticula=1,masa=1, rapidez= 1)
    fig = 0
    
    
    
    dicprotones = {
    "Protón": 1,
    "Positrón": 1,
    "Berilio-8": 4,
    "Helio-5": 2,
    "Alfa triplemente cargada": 2,
    "Núcleo de carbono" : 6,
    "Núcleo de oxígeno" : 8

    }
    
    dicneutrones = {
    "Protón": 1,
    "Positrón": 1,
    "Berilio-8": 4,
    "Helio-5": 3,
    "Alfa triplemente cargada": 2,
    "Núcleo de carbono" : 6,
    "Núcleo de oxígeno" : 8

    }

    dicColors = {
    "Protón": "#FF0000",
    "Positrón": "#00FF00",
    "Berilio-8": "#0000FF",
    "Helio-5": "#FFFF00",
    "Alfa triplemente cargada": "#FFC0CB",
    "Núcleo de carbono" : "#FFA500",
    "Núcleo de oxígeno" : "#800080",
    "Personalizado" : "#00FFFF"
    }
   
    
    root = tk.Tk()
    eleccion = tk.IntVar()
    names = ["Protón", "Positrón", "Berilio-8", "Helio-5", "Alfa triplemente cargada", "Núcleo de carbono", "Núcleo de oxígeno","Personalizado"]

    particula = tk.StringVar()
    particula.set(names[0])
## Helio-4, que consta de dos protones y dos neutrones
##Alfa triplemente cargada: compone de dos protones y un neutrón y tiene una carga eléctrica de +3e
## El berilio-8 es un núcleo inestable compuesto por cuatro protones y cuatro neutrones.
    entryradio = tk.Entry(root)
    entrycargaesfera = tk.Entry(root)
    entrydens = tk.Entry(root)
    

    
    canvas = tk.Canvas(root)
    canvas.config(width=800, height=600)
    canvas.grid(row=1,column=1,rowspan=40, columnspan=2 )
    screen = turtle.TurtleScreen(canvas)
    tortu = RawTurtle(screen) #Tortuga de desplazamiento
    tortu.width(3)
    planos = turtle.RawTurtle(screen, shape="arrow")
    planos.hideturtle()
    esferas = turtle.RawTurtle(screen, shape="arrow")
    esferas.hideturtle()
    tortu = RawTurtle(screen)
    pantalla()
    tk.Label(root, text="Calculo de velocidad de una párticula", font=("Arial", 16)).grid(row=0,column=1, columnspan=2)
    tk.Label(root, text="Seleccione el tipo de carga central fija", font=("Arial", 12)).grid(row=1,column=0)
    c1 = tk.Radiobutton(root, text='Esfera',variable=eleccion, value=1, font=("Arial", 10), command= lambda: check_button_command(entrycargaesfera) ).grid(row=2,column=0)
    c2 = tk.Radiobutton(root, text='Plano',variable=eleccion, value=2, command= lambda: check_button_command(entrycargaesfera), font=("Arial", 10) ).grid(row=3, column=0)
    
    

    datos = tk.Label(root, text="Esperando la selección de la carga central....", font=("Arial", 8))
    datos.grid(row=4,column=0)    

    dato1 = tk.Label(root, font=("Arial", 10))
    dato1.grid(row=5,column=0)
    dato2 = tk.Label(root)
    dato2.grid(row=7,column=0)
   
    


    tk.Label(root, text="Seleccione la partícula que quiera disparar", font=("Arial", 12)).grid(row=10,column=0)
    nombrepart = tk.OptionMenu(root, particula ,*names, command = lambda _: seleccionar_elementos(particula.get())).grid(row=11, column=0)
    nombrepart = particula.get()
    tk.Label(root, text="Datos Importantes", font=("Arial", 12)).grid(row=22,column=0)
    charge = tk.Label(root, text="Ingrese la carga", font=("Arial", 12))
    entrycargapart = tk.Entry(root)
    massLabel = tk.Label(root, text="Ingrese la masa", font=("Arial", 12))
    masa = tk.Entry(root)
    speedLabel = tk.Label(root, text="Ingrese la rapidez inicial", font=("Arial", 12))
    speedLabel.grid(row=27,column=0)

    errur = tk.Label(root, text="", font=("Arial", 12))
    errur.grid(row=12, column=0)

    rapidez = tk.Entry(root)
    rapidez.grid(row=28, column=0)
    
    tortu = RawTurtle(screen)
    submit = tk.Button(root, text="Generar Resultados...", command= lambda: meterdatos(fig, entrycargapart.get(),masa.get(), rapidez.get(),entryradio.get(),entrycargaesfera.get(),entrydens.get(), particula.get(), eleccion.get(), tortu))
    submit.grid(row=30,column=0)

    velo = tk.Label(root, text="Rapidez inicial: " + str(0) + "m/s", font=("Arial", 12))
    velo.grid(row=41,column=1)

    veloEscape = tk.Label(root, text="Velocidad de escape: " +str(0) + "m/s", font=("Arial",12))

    dist = tk.Label(root, text="Distancia de máximo alejamiento: " + str(0) + "metros", font=("Arial", 12))
    dist.grid(row=41,column=2)

    parte = tk.Label(root, text="Particula: " + str(nombrepart) , font=("Arial", 12))
    parte.grid(row=42,column=1)

    borrar = tk.Button(root, text="Borrar particula", font=("Arial", 12),  command= lambda: eliminarrecorrido(tortu))
    borrar.grid(row=42,column=2)


    root.mainloop()