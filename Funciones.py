import math

#plano
#Velocida de escape
def escapeV(mass, cargaEsfera, radio, particula, protones, neutrones):
    energia = abs((float(cargaEsfera)*(float(protones)*float(1.6*10**-19)))/(4*3.14*8.85*10**-12*float(radio)))**1/2
    mass = float(protones*1.67*10**-27) + float(neutrones*1.67*10**-27)
    return ((2*float(energia)/float(mass))**1/2)

#Distancia plano infinito
def distanceP(velocity, density, protons, neutrons, particula):
    if particula == "Positrón":
        return abs(((float(protons)+float(neutrons))*(9.11*10**-31)*float(velocity)**2*(8.85*10**-12))/(float(protons)*(1.6*10**-19)*float(density)))
    else :
        return abs(((float(protons)+float(neutrons))*(1.67*10**-27)*float(velocity)**2*(8.85*10**-12))/(float(protons)*(1.6*10**-19)*float(density)))

#Distancia esfera
def distanceS(radio, protons, neutrons, velocity, particula, cargaEsfera):
    if particula == "Positrón":
        return abs((2*math.pi*(8.85*10**-12)*float(radio)**2*(float(protons)+float(neutrons))*(9.11*10**-31)*float(velocity)**2)/(float(protons)*(1.6*10**-19)))
    else :
        return abs((2*math.pi*(8.85*10**-12)*float(radio)**2*(float(protons)+float(neutrons))*(1.67*10**-27)*float(velocity)**2)/(float(protons)*(1.6*10**-19)))
    
#Distancia plano infinito particula personalizada
def distancePP(velocity, density, masa, carga):
    return abs((float(masa)*float(velocity)**2*(8.85*10**-12))/(float(1.6**10-19)*float(density)))

#Distancia esfera particula personalizada
def distanceSP(radio, masa, velocity, carga, cargaEsfera):
    return abs((2*math.pi*(8.85*10**-12)*float(radio)**2*float(1.6**10-19)*float(velocity)**2)/1.6**10-19*float(cargaEsfera))

#Detrminación de decimales
def decimals(numero):
    numero_str = str(numero)

    if 'e' in numero_str:
        partes = numero_str.split('e')
        parte_principal = partes[0]
        cantidad_decimales = len(parte_principal.split('.')[1])
        return cantidad_decimales
    else :
        if "." in numero_str:
            partes = numero_str.split(".")
            cantidad_decimales = len(partes[1])
            return cantidad_decimales
        else:
            return 0