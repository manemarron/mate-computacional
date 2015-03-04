#funcion para desponer un arreglo de 9x9 en 9 subarreglos de 3x3
#inicializo un arreglo con zeros para guardar en el mismo el arreglo que se
#va a descomponer
#Me pasa igual que con la criba de erastotenes no logro hacer que 
#reconazca el argumento, pero si funciono, antes de declararla como funcion
import numpy as np
arraysepar = np.zeros((3,3,3,3))
def descomponer(x):
   for i in range(0,9,3):
        for j in range(0, 9,3):
            arraysepar[i/3,j/3,0:3,0:3] = x[i:i+3, j:j+3]
#se van guardando los arreglos de 3x3 en cada una de los subarreglos del 
#arreglo declarado inicialmente con ceros, dejo fijo los indices finales
#porque de antemano para este ejercicio conozco las dimensiones del arreglo
print arraysepar
