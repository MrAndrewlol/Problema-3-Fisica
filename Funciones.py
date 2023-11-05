import math

#Resistencia del alambre
def resistance(resistivity,length,diameter): #Recibe como parametros la resistividad del material, el largo del cable (m) y su diametro (mm)
    resistance = (4*resistivity*length)/(math.pi*(diameter*10**-3))
    return resistance

#AWG Converter
def converter(AWG): #Recibe el número de AWG en String
    mm = 0
    if AWG == "0000":
        mm = 11.684
    elif AWG == "000":
        mm = 10.405
    elif AWG == "00":
        mm = 9.266
    else :
        mm = 0.127*92**((36-AWG)/39)

    return round(mm, 3) 