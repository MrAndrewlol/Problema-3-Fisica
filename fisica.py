import customtkinter as CTK
import turtle
from turtle import RawTurtle, ScrolledCanvas
import tkinter as tk

import pruebas as pr

CTK.set_appearance_mode("System")  # Modes: system (default), light, dark
CTK.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


###Array
prefix = ["M", "k", "h", "da", "d", "c", "m","μ", "n", "p" ]
dicprefix = {  }
awg = ["AWG 4", "AWG 6","AWG 8","AWG 10", "AWG 12","AWG 14", "AWG 16", "AWG 18", "AWG 20", "AWG 22"]

mater = ["oro", "plata", "cobre", "aluminio", "grafito"]



app = CTK.CTk()  # create CTk window like you do with the Tk window
app.geometry("1530x1080+0+0") #1920 -1080
canvas = tk.Canvas(app)
canvas.config(width=1200, height=700) ##Cambiar la resolucion de la pantalla de la tortuga
canvas.grid(row=10,column=10,rowspan=40, columnspan=4 )

screen = turtle.TurtleScreen(canvas)
tortugagrid = RawTurtle(screen) 





# Use CTkButton instead of tkinter Button
titulo = CTK.CTkLabel( app,text="Rapidez de arrastre de los electrones", font=("Arial", 30))
titulo.grid(row=0, column = 4, columnspan=3)


##Entradas de largo de alambre
largoal = CTK.CTkLabel( app,text="Largo del alambre (metros)", font=("Arial", 16))
largoal.grid(row=50, column = 4)
entrylargo = CTK.CTkEntry(app)
entrylargo.grid(row=50, column=5)
optionmenu_var = CTK.StringVar(value="m")
optionmenu = CTK.CTkOptionMenu(app,values=prefix, variable=optionmenu_var)
optionmenu.grid(row=50, column=7)

##Entradas Diametro
tawg = CTK.CTkLabel( app,text="Diámetro (mm)", font=("Arial", 16))
tawg.grid(row=51, column = 4)
awgentry = CTK.StringVar()
awg = CTK.CTkComboBox(app, values=awg, state="normal", variable=awgentry )
awg.grid(row=52, column = 4)

##Entradas material Conductor
cond = CTK.CTkLabel( app,text="Diámetro (mm)", font=("Arial", 16))
cond.grid(row=53, column = 4)
materia = CTK.StringVar()
maters = CTK.CTkComboBox(app, values=mater, state="readonly", variable=materia ) ##escribi la densidads
maters.grid(row=54, column = 4)

##Entradas voltaje aplicado
voltage = CTK.CTkLabel( app,text="Voltaje a aplicar", font=("Arial", 16))
voltage.grid(row=55, column = 4)
voltd =  CTK.CTkEntry(app) ##escribi la densidads
voltd.grid(row=56, column = 4)



pr.pantalla(tortugagrid)

app.mainloop()