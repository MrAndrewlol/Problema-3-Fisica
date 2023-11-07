import math

#Resistance
def resistance(resistivity,length,diameter): #Params: resistivity (Ohms*m), length (m), diameter (mm)
    resistance = (4*resistivity*length)/(math.pi*((diameter*10**-3)**2))
    return round(resistance,2)

#AWG Converter
def converter(AWG): #Params: AWG number in String
    mm = 0
    if AWG == "0000":
        mm = 11.684
    elif AWG == "000":
        mm = 10.405
    elif AWG == "00":
        mm = 9.266
    else :
        mm = 0.127*92**((36-AWG)/39)

    return round(mm, 2) 

#Current 
def current(voltage, resistance): #Params: voltage (V), resistance (Ohms)
    return round(voltage/resistance,2)

#Power
def power(voltage,current): #Params: voltage (V), current (A)
    return round(voltage*current,2)

#drag speed
def dSpeed(current,particleDensity,diameter): #Params: current (A), particle density (electrons/m^3), diameter (mm)
    return round((4*current)/(particleDensity*(1.60*10**-19)*((diameter*10**-3)**2)),4)

#time
def time(length,dSpeed): #Params: length (m), drag speed (m/s)
    return round(length/dSpeed,2)