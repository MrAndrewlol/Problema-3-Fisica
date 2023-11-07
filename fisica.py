import customtkinter as CTK
import turtle
from turtle import RawTurtle, ScrolledCanvas
import tkinter as tk
import Funciones as func
import pruebas as pr

CTK.set_appearance_mode("System")  # Modes: system (default), light, dark
CTK.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


def calculardatos(largo, largoprefijo,diametro, voltaje, material):
    if(int(largo) != 0 and diametro !=0 and int(voltaje) !=0):
        print("exitos")
        try:
            integer_number = int(diametro)
            largo = float(largo)*dicprefix[largoprefijo]
            print(f"The integer value is: {integer_number}")
            resistencia = func.resistance(float(dicmater[material]), float(largo), float(dicawg[diametro]))
            resis.configure(text= " "+ str(resistencia) +" Ω")
            corriente = func.current(float(voltaje), float(resistencia))
            corr.configure(text=" " + str(corriente) + " A")
            rapidez = func.dSpeed(float(corriente),1,float(diametro) )
            rapi.configure(text= " " + str(rapidez) + " m/s" )
            tiempo = func.time(float(largo),float(rapidez))
            tiemp.configure(text=" "+ str(tiempo) + " s")
            pr.cilindro(tortu2, largo, float(diametro))
            pr.movelectron(tortu3, tortu4, tortu5, tortu6, float(diametro)/2, largo, tiempo%4, rapidez%11)
        except ValueError:
            print("The string does not represent a valid integer.")
            resistencia = func.resistance(float(dicmater[material]), float(largo), float(dicawg[diametro]))
            resis.configure(text= " "+ str(resistencia) +" Ω")
            corriente = func.current(float(voltaje), float(resistencia))
            corr.configure(text=" " + str(corriente) + " A")
            rapidez = func.dspeed(float(corriente),1,float(diametro) )
            rapi.configure(text= " " + str(rapidez) + " m/s" )
            tiempo = func.time(float(largo),float(rapidez))
            tiemp.configure(text=" "+ str(tiempo) + " s")
            pr.cilindro(tortu2, largo, float(diametro))
            pr.movelectron(tortu3, tortu4, tortu5, tortu6, float(diametro)/2, largo, tiempo%4, rapidez%11)

        
            

        
    



###Array
prefix = ["M", "k", "h", "da", "d", "--","c", "m","μ", "n", "p" ]
dicprefix = { "M": 1*10**6, "k": 1*10**3, "h": 1*10**2, "da": 1*10**1, "--": 1 , "d": 1*10**-1, "c": 1*10**-2, "m": 1*10**-3, "μ": 1*10*-6, "n": 1*10*-9, "p": 1*10*-12 }
awg = ["AWG 4", "AWG 6","AWG 8","AWG 10", "AWG 12","AWG 14", "AWG 16", "AWG 18", "AWG 20", "AWG 22"]
dicawg = {"AWG 4": 5.189, "AWG 6": 4.115,"AWG 8": 3.264,"AWG 10" : 2.588, "AWG 12" : 2.053,"AWG 14": 1.628, "AWG 16": 1.291, "AWG 18" : 1.024, "AWG 20" : 0.812, "AWG 22" : 0.643}
mater = ["oro", "plata", "cobre", "aluminio", "grafito"]
dicmater = {"oro":1, "plata" : 1, "cobre" :1, "aluminio": 1, "grafito": 1}
dicmateresis = {"oro":2.35*10**-8, "plata" : 1.59*10**-8, "cobre" :1.79*10**-8, "aluminio": 2.82*10**-8, "grafito": 60.00*10**-8} #Resistividad ohms por metro





app = CTK.CTk()  # create CTk window like you do with the Tk window
app.geometry("1530x1080+0+0") #1920 -1080
despx = 190

app.columnconfigure(100, weight=0)
app.rowconfigure(100, weight=0)

##Marco para salidas
frame = CTK.CTkFrame(app)
frame.rowconfigure(25, weight=1)
frame.columnconfigure(25, weight=1)
frame.grid(row=4,column=25, columnspan= 25, rowspan=25, sticky= "n")

##Marco para entradas
entryframe = CTK.CTkFrame(app)
entryframe.rowconfigure(25, weight=2)
entryframe.columnconfigure(25, weight=2)
entryframe.grid(row=4,column=0, columnspan= 25, rowspan=25, sticky= "n")




#Marco para salidas

# Use CTkButton instead of tkinter Button
titulo = CTK.CTkLabel( app,text=" ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬", font=("Arial", 14))
titulo.grid(row=0,column=0, columnspan = 50)
titul1 = CTK.CTkLabel( app,text="● • ● • ● • ● ● • ● • ● • ● Rapidez de arrastre de los electrones • ● • ● • ● • ● ● • ● • ● • ●", font=("Arial", 16))
titul1.grid(row=1,column=0, columnspan = 50)
titulo2 = CTK.CTkLabel( app,text=" ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬", font=("Arial", 14))
titulo2.grid(row=2,column=0, columnspan = 50)

canvas = tk.Canvas(app)
canvas.config(width=1920, height=500) ##Cambiar la resolucion de la pantalla de la tortuga
canvas.grid(row=3,column=0, columnspan=100)

screen = turtle.TurtleScreen(canvas)
tortugagrid = RawTurtle(screen) 

tortu2 = RawTurtle(screen)
tortu3 = RawTurtle(screen).color("yellow")
tortu4 = RawTurtle(screen).color("yellow")
tortu5 = RawTurtle(screen).color("yellow")
tortu6 = RawTurtle(screen).color("yellow")





tituloentrys = CTK.CTkLabel( entryframe,text="Entradas", font=("Arial", 18))
tituloentrys.grid(row=0,column=0, columnspan= 25)

titulosalida = CTK.CTkLabel( frame,text="Salidas", font=("Arial", 18))
titulosalida.grid(row=0,column=25, columnspan= 25)

columndesp = 10
##Entradas de largo de alambre
largoal = CTK.CTkLabel( entryframe,text="        Largo del alambre (metros)", font=("Arial", 14))
largoal.grid(row=1, column = columndesp)
entrylargo = CTK.CTkEntry(entryframe, placeholder_text="0.0 m")
entrylargo.grid(row=2, column=columndesp)
optionmenu_var = CTK.StringVar(value="n")
optionmenu = CTK.CTkOptionMenu(entryframe,values=prefix, variable=optionmenu_var, width=10 )
optionmenu.grid(row=2, column=columndesp+1, sticky="w")

##Entradas Diametro
tawg = CTK.CTkLabel( entryframe,text="Diámetro (mm)", font=("Arial", 14))
tawg.grid(row=4, column = columndesp, sticky="s")
awgentry = CTK.StringVar(value="AWG 4")
awg = CTK.CTkComboBox(entryframe, values=awg, state="normal", variable=awgentry )
awg.grid(row=5, column = columndesp)

##Entradas material Conductor
cond = CTK.CTkLabel( entryframe,text="Material del conductor", font=("Arial", 14))
cond.grid(row=4, column = columndesp+3, sticky="s")
materia = CTK.StringVar(value="oro")
maters = CTK.CTkComboBox(entryframe, values=mater, state="readonly", variable=materia ) ##escribi la densidads
maters.grid(row=5, column = columndesp+3)

##Entradas voltaje aplicado
voltage = CTK.CTkLabel( entryframe,text="Voltaje a aplicar (V)", font=("Arial", 14))
voltage.grid(row=1, column = columndesp+3)
voltd =  CTK.CTkEntry(entryframe, placeholder_text="0.0 V") ##escribi la densidads
voltd.grid(row=2, column = columndesp+3)


CTK.CTkLabel( entryframe,text="\n             \n", font=("Arial", 14)).grid(row=3, column=columndesp+2) #Espaciado
CTK.CTkLabel( entryframe,text="        ", font=("Arial", 14)).grid(row=7, column=columndesp+5) #Espaciado
#BUTON
buton = CTK.CTkButton(entryframe, text="Calcular y dibujar", command=lambda: calculardatos(entrylargo.get(), optionmenu_var.get(), awgentry.get(),voltd.get() ,maters.get()  ))
buton.grid(row= 8, column=columndesp+1, sticky="n")

##Parametros de Salida 

##Resistencia del alambre
CTK.CTkLabel( frame,text="Resistencia del alambre", font=("Arial", 16)).grid(row=1, column=25, columnspan= 25)
resis = CTK.CTkLabel( frame,text="0 Ω", font=("Arial", 16))
resis.grid(row=2,column=25, columnspan= 25)

#Corriente
CTK.CTkLabel( frame,text="Corriente", font=("Arial", 16)).grid(row=3, column=25, columnspan= 25)
corr = CTK.CTkLabel( frame,text="0.0 A", font=("Arial", 16))
corr.grid(row=4,column=25, columnspan= 25)


#velocidad
CTK.CTkLabel( frame,text="Rapidez de arrastre de los electrones", font=("Arial", 16)).grid(row=5, column=25, columnspan= 25)
rapi = CTK.CTkLabel( frame,text=" 0 m/s", font=("Arial", 16))
rapi.grid(row=6,column=25, columnspan= 25)

#tiempo
CTK.CTkLabel( frame,text="     Tiempo que le tomará a los electrones atravesar todo el alambre         ", font=("Arial", 16)).grid(row=7, column=25, columnspan= 25)
tiemp = CTK.CTkLabel( frame,text=" 0 s", font=("Arial", 16))
tiemp.grid(row=8,column=25, columnspan= 25)

##APARTADO



pr.pantalla(tortugagrid)

app.mainloop()