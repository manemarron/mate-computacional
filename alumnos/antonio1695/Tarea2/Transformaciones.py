""" Programa que transforma coordenadas cartesianas en coordenadas esfericas"""
import math
def transformaciones(x,y,z):
    rho = math.sqrt(x**2 + y**2 + z**2) # Conversion de x a esférica.
    theta = math.atan(y/x) # Conversion de y a esférica.
    phi = math.atan((rho/z)) # Conversion de z a esférica.
    esferica = [rho,theta,phi] 
    
    return esferica