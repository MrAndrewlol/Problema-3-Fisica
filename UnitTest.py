import Funciones as func

#Prueba Resistencia


#Prueba AWG Converter
def converterTest():
    conversion = func.converter(14)
    if conversion == 1.628:
        return True
    else :
        return False
    
print(converterTest())

#Prueba de resistencia
def resistenciaTest():
    resistencia = func.resistance(1.79*10**-8,30,func.converter(14))
    if resistencia == 0.26:
        return True
    else :
        return False
    
print(resistenciaTest())