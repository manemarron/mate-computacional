# -*- coding: utf-8 -*-
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

class RegresionLineal:
    def __init__(self, alpha=0.3, max_iters=100, tols=0.001):
        """
        Parámetros.
        ---------------
        alpha = Learning rate
        max_iters = Número máximo de iteraciones
        tols = definición de convergencia
        """
        self.alpha = alpha
        self.max_iters = max_iters
        self.tols = tols
        self.breaking_iteration = None
        self.historia = {'costo':[], 'beta':[]}  # Con fines de graficación
        
    def gradientDescent(self, x, y):
        """
        Parámetros:
        ---------------
        x = vector de entrenamiento de features
        y = vector de entrenamiento de variable a predecir (target)
        """    
        
        # ajustamos el vector de features
        unos = np.ones((x.shape[0], 1))
        Xt = x.reshape(x.shape[0], 1)
        Xt = np.concatenate((unos, Xt), axis=1)
        
        i = 0
        prep_J = 0
        m, n = Xt.shape
        self.beta = np.zeros(n) 
        
        while i < self.max_iters:     
            # Actualizamos beta
            self.beta = self.beta - self.alpha * self.gradiente(Xt, y)
            
            J = self.costo(Xt, y)
            
            if abs(J - prep_J) <= self.tols:
                print 'La función convergió con beta: %s en la iteración %i' % ( str(self.beta), i )
                self.breaking_iteration = i
                break
            else:
                prep_J = J
            
            self.historia['costo'].append(J)
            self.historia['beta'].append(self.beta)                
            i += 1
    
    def hipotesis(self, x):
        return np.dot(x, self.beta)
    
    def costo(self, x, y):
        m = x.shape[0]
        error = self.hipotesis(x) - y
        return np.dot(error.T, error) / (2 * m) 
    
    def gradiente(self, x, y):
        m = x.shape[0]
        error = self.hipotesis(x) - y        
        return np.dot(x.T, error) / m    

    def plotModelo(self, x,y,iteracion):
        modelo = lambda x,b,m: b + m*x # función para graficar el modelo
    
        _beta = self.historia['beta'][iteracion]

        fig, ax = plt.subplots(1,2, figsize=(10,6))
        ax[0].scatter(x,y, label="datos")
        ax[0].plot(x, modelo(x, _beta[0], _beta[1]), label="int: %1.2f, pen: %1.2f" % (_beta[0], _beta[1]))
        ax[0].set_xlabel('Datos x')
        ax[0].set_ylabel('Datos y')
        ax[0].legend(loc="best")
        #ax[0].set_xlim(0, max(x))
        #ax[0].set_ylim(0, max(y))
    
        costo  = self.historia['costo']
    
        iteraciones = [i for i in range(0, len(costo))]
        ax[1].plot(iteraciones, costo, 'g', label="costo")
        ax[1].plot(iteracion, costo[iteracion], 'or', label="iteracion")
        ax[1].set_xlabel('Iteraciones')
        ax[1].set_ylabel('Costo')
        ax[1].legend(loc="best")
