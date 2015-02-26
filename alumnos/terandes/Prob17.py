nameNum = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand']
#Creo que me complique demasiado, pero por fin quedo, utilizo varios contadores para 
#las diferentes partes donde se van requiriendo los mismos. Coloque muchas impresiones
#porque como de costumbre no se ejecuta sin errores a la primera
letrasNum = 0
k = 1
i = 1
j = 0
h = 2
m = 0
n = 0
s = 0
t = 0
while k <= 1000:
#Primero suma sobre aquellos numeros que van del 1-20, para cuando i=1 y n=0
#busco en la lista inicial para convertir el nombre del número en dígitos
    if k >= (n*10**i)+1 and k <= (20 + n*10**i):
        if i == 1:
            numk = str(nameNum[k-1])
            letrasNum = int(len(numk)) + letrasNum
            #print numk
            #print letrasNum
#luego se suma para cuando k va de 101-120, 201-220, 301-320 y sucesivamente
        if i != 1 and s <= 19:
#numk10 corresponde a las centenas
            numk = numk10 + str(' ') + str('and') + str(' ') + str(nameNum[s])
            letrasNum = int(len(numk)) + letrasNum-3
            s += 1 
        j = 0
#aqui ya se construyen los numeros por decenas con el guion por lo cual es diferente
#de los 1eros 20 de cada centena, y solo se busca en las posiciones del 0 al 8 en la
#lista declarada inicialmente. Igual que arriba primero lo realizo para k entre 21-99
#sin tomar en cuenta las decenas
    if k >= (20 + n*10**i) and j <= 8:
        #j = 0
        if i == 1:
            numk = str(nameNum[19+m]) + str('-') + str(nameNum[j])
#resto uno por el guion
            letrasNum = int(len(numk)) + letrasNum-1
            #j += 1
            #print letrasNum
            j += 1
        #t = 0
#para cuando ya se llega a las centenas nuevamente uso numk10
        if i != 1 and t <= 8:
            numk=numk10+str(' ')+str('and')+str(' ')+str(nameNum[19+m])+ str('-') + str(nameNum[t])
#resto 4 por los 3 espacios (1 contenido en numk10) y el del guion
            letrasNum = int(len(numk)) + letrasNum-4
            t += 1
#lo siguiente es para las decenas exactas primero paras las contenidas de 1-99
#disminuye la cuenta del contador de 8 a 7 por que del 1-20 ya se conto previamente
#por lo que solo quedan 7 decenas
    if k == ((h+1)*10 + n*10**i) and m < 7:
        t = 0
        m +=1
        if k != 100*(h-1) and i == 1:
            decena = str(nameNum[19+m])
            letrasNum = int(len(str(decena))) + letrasNum
# lo siguiente es para las decenas contenidas en las restantes centenas del 100-999
#y por lo tanto es necesario nuevamente usar: numk10 la correspondiente a cada centena
        if i != 1:
            numk=numk10+str(' ')+str('and')+str(' ')+str(nameNum[19+m])
#resto 3 por los espacios y el que esta en numk10
            letrasNum = int(len(numk)) + letrasNum-3
        j = 0
        h += 1
#para contar la cantidad de letras en las centenas es un poco sencillo, aquí es donde
#se declara numk10. Se resta 1 por el espacio entre el número y el hundred
    if k == 100*(n+1) and n < 9:
        h = 2
        t = 0
       # print "se llega a las centenas"
        numk10 = str(nameNum[n]) + str(' ') + str(nameNum[20+m])
        letrasNum = int(len(numk10)) + letrasNum -1
        #print letrasNum
        n += 1
        i = 2
        m = 0
        s = 0
#para contar mil ya solo sume las celdas necesarios de la lista
    if k == 1000:
        letrasNum = int(len(nameNum[0]))+int(len(nameNum[28])) + letrasNum
    k += 1
print letrasNum
