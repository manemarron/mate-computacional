#Funcion para cambiar un número entero de decimal a binario. Intente incluir
#la funcion de assert, pero no encontre el error porque cuando la dejaba no se
#realizaba la operación, supuse que era porque no podía obtener el valor de la
#longitud de la cadena, pero tampoco fue eso, por eso lo deje comentado
def binario(x):
    b2 = str()          #inicializo una cadena vacia para almacenar los 
                        #valores del número en base 2
    while abs(x) >=1:
        j = x%2
        b2 = str(j) + b2 #se va construyendo el numero binario
        x = x/2          #el nuevo numero sobre el cual obtener mod2
        b2s = str(b2) 
        #assert len(b2s) > 127, 'Overflow'
        #print len(b2s)
    print "El número decimal x en binario es:", b2s
