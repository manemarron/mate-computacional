
class RegresionLineal:
    def __init__(self, alpha=0.3, max_iters=100, tols=0.001): #constructor
        """
        Parametros
        ---------------
        alpha = Learning rate
        max_iters = Numero maximo de iteraciones
        tols = definicion de convergencia
        """
        self.alpha = alpha
        self.max_iters = max_iters
        self.tols = tols
        self.breaking_iteration = None
        self.historia = {'costo':[], 'beta':[]}  # Con fines de graficacion
        
    def gradientDescent(self, x, y):
        """
        Parametros:
        ---------------
        x = vector de entrenamiento de features
        y = vector de entrenamiento de variable a predecir (target)
        """    
        
        # ajustamos el vector de features
        unos = np.ones((x.shape[0], 1))
        Xt = X.reshape(x.shape[0], 1)
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
                print 'La funcion convergio con beta: %s en la iteracion %i' % ( str(self.beta), i )
                self.breaking_iteration = i
                break
            else:
                prep_J = J
            
            self.historia['costo'].append(J)
            self.historia['beta'].append(self.beta)   
            i += 1
    
    def hipotesis(self, x):
        return np.dot(x, self.beta) #producto punto
    
    def costo(self, x, y):
        m = x.shape[0]
        error = self.hipotesis(x) - y
        return np.dot(error.T, error) / (2 * m) 
    
    def gradiente(self, x, y):
        m = x.shape[0]
        error = self.hipotesis(x) - y        
        return np.dot(x.T, error) / m    
    
    #mio
    def plot(X, interceptor, pendiente, alfa):
        modelo = lambda x,b,m: b + m*x # funcion para graficar el modelo
    