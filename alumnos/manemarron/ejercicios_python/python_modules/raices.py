import sympy as sym
import numpy as np

def deriv_Atras(f,x0,x1):
    return (f(x0)-f(x1))/float(x0-x1)

def deriv_H(f,x0,h):
    return (f(x0+h)-f(x0))/float(h)

def newton_lambda(f,x0,tolerance,stop=50):
    df = lambda x: (f(x + 0.001)-f(x)) / 0.001
    
    k=0
    diff=1
    while diff >= tolerance and k < stop:
        k = k+1
        x1 = x0 - (f(x0)/df(x0))
        diff = abs(x1-x0)
        x0 = x1
    return x0 if k<stop else None

def secante(f,df,x1,x0,tolerance,stop,step):
    if step > stop: return None
    if abs(x1-x0) < tolerance: return x1
    aux = x1
    x1 = x1 - (f(x1)/df(x1,x0))
    x0 = aux
    return secante(f,df,x1,x0,tolerance,stop,step+1)

def newton_sym(f,x, x0, tolerancia, stop):
    assert type(f).__bases__[0]  in (sym.expr.Expr, sym.operations.AssocOp), "La función no es una expresión simbólica ... :/"
    
    # Derivamos la expresión
    df = sym.diff(f, x)
    
    # Convertimos en funciones las expresiones
    F = sym.lambdify(x,f, modules="numpy")
    DF = sym.lambdify(x, df, modules="numpy")
    k = 0
    diff = 1
    
    while diff >= tolerancia and k <= stop:
        k = k + 1
        x1 = x0 - (float(F(x0)/DF(x0)))
        diff = abs(x1 - x0)
        x0 = x1
    return x0 if k<=stop else None

def biseccion(func, a, b, tolerancia, stop):
    k = 0
    
    x = (a + b)/2
    
    I = (b - a)/2
    
    assert func(a)*func(b) < 0, "El signo de la función en los extremos debería de ser diferente"
    assert func(a) != 0, "La raíz es %.5f" % a
    assert func(b) != 0, "La raíz es %.5f" % b
    
    while I >= tolerancia and k <= stop:
        k = k + 1
        
        f_x = func(x)
        f_a = func(a)
        f_b = func(b)        
        
        
        if(f_a*f_x < 0):
            a, b = a, x
        elif(f_x*f_b < 0):
            a, b = x, b
        
        x = (a+b)/2
        
        I = (b - a)/2
        
    return x if k<=stop else None