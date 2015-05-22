
# coding: utf-8

# In[185]:

(-2)**7


# In[186]:

2**7 -1


# In[187]:

def minbit(n):
    min = (2**7)-1
    return min


# In[188]:

def maxbit(n):
    max = -(2)**(n-1)
    return max


# In[189]:

maxbit(8)


# In[190]:

minbit(8)


# In[191]:

get_ipython().show_usage()


# In[192]:

def decaBin(n):
    bina = ""
    max = 127
    if n<max:
        if n==1:
            bina ="1"+bina
            return bina    
        else:
            if n%2==0:
                bina = "0" + bina
            else:
                bina = "1" + bina
        
        return decaBin(n/2) + bina
    else:
        return "Overflow"
    


# In[193]:

decaBin(10)


# In[194]:

"""Esta función de decimal a binario no la voy a limitar para poder utilizarla eficázmente al quere convertir de hexadecimal a
binario"""
def decaBin2(n):
    bina = ""
    if n==1:
        bina ="1"+bina
        return bina    
    else:
        if n%2==0:
            bina = "0" + bina
        else:
            bina = "1" + bina
        
    return decaBin2(n/2) + bina


# In[195]:

def binaDec(n):
    decimal = 0
    for digito in str(n):
        decimal = decimal*2 + int(digito)
    print decimal


# In[196]:

binaDec(1010)


# In[258]:

""" En general el algoritmo es prácticamente el mismo que el utilizado con el binario. La diferencia es que, en vez de existir 
2 caracteres posibles para las congruencias y para la impresión, existen 16 (incluyendo el 0). Por ello la existencia de tantos
ifs. Intenté, previamente, utilizar algún tipo de switch()-case pero no encontré el equivalente en python (seguro por ignoran-
cia y no porque no exista jaja). Google me sugirió utilizar diccionarios pero no me corría bien la función, por ende, recurrí
al clásico truco de utilizar montonales de ifs..."""

def decaHex(n):
    hexa = ""
    
    if n<16:
        if n<10:
            hexa = str(n) + hexa
            return hexa
        else:
            if n == 10:
                hexa = "A" + hexa
                return hexa
            else:
                if n == 11:
                    hexa = "B" + hexa
                    return hexa
                else:
                    if n == 12:
                        hexa = "C" + hexa
                        return hexa
                    else:
                        if n == 13:
                            hexa = "D" + hexa
                            return hexa
                        else:
                            if n ==14:
                                hexa = "E" + hexa
                                return hexa
                            else:
                                    hexa = "F" + hexa
                                    return hexa
    else:
        cong = n%16
        
        if cong == 0:
            hexa = str(cong) + hexa
        else:
            if cong == 1:
                hexa = str(cong) + hexa
            else:
                if cong ==2:
                    hexa = str(cong) + hexa
                else:
                    if cong==3:
                        hexa = str(cong) + hexa
                    else:
                        if cong==4:
                            hexa = str(cong) + hexa
                        else:
                            if cong==5:
                                hexa = str(cong) + hexa
                            else:
                                if cong==6:
                                    hexa = str(cong) + hexa
                                else:
                                    if cong==7:
                                        hexa = str(cong) + hexa
                                    else:
                                        if cong==8:
                                            hexa = str(cong) + hexa
                                        else:
                                            if cong==9:
                                                hexa = str(cong) + hexa
                                            else:
                                                if cong==10:
                                                    hexa = "A" + hexa
                                                else:
                                                    if cong==11:
                                                        hexa = "B" + hexa
                                                    else:
                                                        if cong==12:
                                                            hexa = "C" + hexa
                                                        else:
                                                            if cong==13:
                                                                hexa = "D" + hexa
                                                            else:
                                                                if cong==14:
                                                                    hexa = "E" + hexa
                                                                else:
                                                                        hexa = "F" + hexa
        return decaHex(n/16) + hexa
                


# In[257]:

decaHex(1455)


# In[199]:

def hexaDec(n):
    decimal = 0
    for digito in str(n):
        if str(digito) == "A":
            digito = 10
        else:
            if str(digito) == "B":
                digito = 11
            else:
                if str(digito) == "C":
                    digito = 12
                else:
                    if str(digito) == "D":
                        digito = 13
                    else:
                        if str(digito) == "E":
                            digito = 14
                        else:
                            if str(digito) == "F":
                                digito = 15
    decimal = decimal*16 + int(digito)
    print decimal

# Intenté utilizar un algoritmo parecido al de binarios pero fracasé miserablemente


# In[200]:

hexaDec("10")


# In[212]:

#Por suerte python tiene un convertidor incluido :P
def hexaDec2(n):
    x = int(n, 16)
    return x


# In[213]:

hexaDec2("5AF")


# In[203]:

#Ya que puedo transformar a gusto entre hex-decimal y de dec-bin puedo crear una que transform de hex-bin y viceversa
def hexaBin(n):
    return decaBin2(hexaDec2(n))


# In[204]:

hexaBin("5AF")


# In[259]:

def binaHex(n):
    b = binaDec(n)
    return decaHex(b)


# In[260]:

binaHex(1010)
# No entiendo por qué no funciona si por separado ambas funciones trabajan adecuadamente...


# In[5]:

get_ipython().run_cell_magic(u'file', u'Transforamciones.py', u'\n# Funci\xf3n que transforma de cartesianas a esf\xe9ricas\n\nimport math\ndef esferica(x,y,z):\n    \n    # Llamemos el vector E=(x,y,z)\n    \n    ro = math.sqrt(x**2+y**2+z**2) #Magnitud de E\n    \n    """"Theta es el \xe1ngulo formado por la proyecci\xf3n de E al plano x,y. Es decir, es el \xe1ngulo formado del eje x al vector \n    (x,y,0). Llamemos "r" a este vector. Se calcula a trav\xe9s de arctang(y/x)"""\n    \n    magr = math.sqrt(x**2+y**2) #Magnitud de r\n    \n    theta = math.atan(y/x)\n    \n    """Notemos que:\n        x = rcos(theta)\n        y = rsen(theta)\n    \n    \n     Phi es el \xe1ngulo del eje z al vector E. Para encontrar phi se considera el vector r. Trasladando r a la altura de \n    la coordenada cartesiana (valor de z del vector E) se puede formar un tri\xe1ngulo rect\xe1ngulo entre el eje z, r trasladada y E\n    (de todas formas lo \xfanico que nos interesa son las magnitudes de dichos catetos) Aplicamos arctan(magr/z) para calcular \n    phi"""\n    \n    phi = math.atan(ro/z)\n    \n    """\n    Notemos que:\n        r = sin(phi)\n    \n    Por lo tanto tenemos que:\n    """\n    \n    x1= ro*math.sin(phi)*math.cos(theta)\n    y1= ro*math.sin(phi)*math.sin(theta)\n    z1= ro*math.cos(theta)\n    \n    return (x1,y1,z1)\n    ')

