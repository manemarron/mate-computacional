"""
    convertir un numero binario a hexadecimal
"""
def BinarioAHexadecimal(binario):
    decimal=int(binario,2)
    hexadecimal = ' '
    
    while decimal//16!=0:
        if decimal %16==10:
            hexadecimal ='A' + hexadecimal
        else:
            if decimal%16 == 11:
                hexadecimal = 'B' + hexadecimal
            else:
                if decimal%16 == 12:
                    hexadecimal = 'C' + hexadecimal
                else:
                    if decimal%16 == 13:
                        hexadecimal = 'D' + hexadecimal
                    else:
                        if decimal%16 == 14:
                            hexadecimal = 'E' + hexadecimal
                        else:
                            if decimal%16==15:
                                hexadecimla = 'F' + hexadecimal
                            else:
                                hexadecimal = str(decimal%16) + hexadecimal
    decimal= decimla//16
    return str(decimal) + hexadecimal
                            
                    