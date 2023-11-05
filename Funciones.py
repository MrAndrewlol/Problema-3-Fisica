import math

#Resistencia del alambre
def resistance(resistivity,length,diameter): #Recibe como parametros la resistividad del material, el largo del cable (m) y su diametro (mm)
    resistance = (4*resistivity*length)/(math.pi*(diameter*10**-3))
    return resistance