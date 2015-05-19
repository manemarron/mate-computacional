
# -*- encoding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import mpl_toolkits.mplot3d.axes3d as a3d

from numpy import sin, cos

from utils import normalizeRads, normalizeAngle
from scipy.integrate import odeint

class Pendulo1_invertido:
    
    def __init__(self,estado_inicial=[0.1,0.,0,0.],
                 m = 0.1, #masa en kg 
                 MP = 2.0, #masa en kg
                 l = 1.0, #longitud en m
                 g = (-1)*9.8, #aceleracion de la gravedad en m/s^2
                 f = 0.6, #lo que en las ecuaciones es c, coeficiente de friccion 
                 b = (-1)*0.3, #lo que en las ecuaciones es b, coeficiente de friccion angular
                 I = 0, #se considera que debido a la masa tan pequeña se suprime la inercia
                 fza = 21.1, #fuerza en N 
                 origen=(0,0)):
        
        self.estado_inicial = np.asarray(estado_inicial, dtype='float')
        self.estado_inicial = normalizeRads(self.estado_inicial, decimals=8) 
        
        self.params = (m,MP,l,g,f,b,I,fza)
        self.origen = origen
        self.time_elapsed = 0

        self.estado = self.estado_inicial

        self.trayectoria = self.estado

        #self.Omega = (g/l)**0.5
        #self.period = 2*np.pi/self.Omega
        #self.masa_tot = Masa_pendulo + masa_carro
        #self.denominador = Masa_pendulo*masa_carro*longitud**2+Inercia*masa_tot
        #self.num_xbiprima = masa_carro*longitud**2 + Inercia
        #self.masa_longitud = masa_carro*longitud

    def y(self):
        (m,MP,l,g,f,b,I,fza)=self.params
        return l*sin(self.theta())
        
    def z(self):
        (m,MP,l,g,f,b,I,fza)=self.params
        return l*cos(self.theta())
        
    def x(self):
        return self.estado[0]

    def xprima(self):
        return self.estado[1]

    def theta(self):
        return self.estado[2]

    def thetap(self):
        return self.estado[3]

    # Ecuaciones de movimiento 
    def dynamics (self, state, t):
        
        (m,MP,l,g,f,b,I,fza)=self.params

        g0 = state[1]
        g1 = (fza*(MP*(l**2)+I)-(1*f)*(MP*(l**2)+I)*state[1]-(1*MP)*l*b*state[3]+(MP**2)*g*(l**2)*state[2])/(I*(m+MP)+m*MP*(l**2))
        g2 = state[3]
        g3 = (fza*MP*l-1*f*MP*l*state[1]-1*b*state[3]*(m+MP)+MP*g*l*state[2]*(MP+m))/(I*(m+MP)+m*MP*(l**2))
        return np.array ([g0, g1, g2 ,g3])
    
    # Calcula la posición actual del péndulo
    
    def position(self):
        
        (m,MP,l,g,f,b,I,fza)=self.params
        y= [self.origen[0], self.origen[0] - l*sin(self.estado[2])]
        z = [self.origen[1], self.origen[1] - l*cos(self.estado[2])]

        return (y,z)      
    
    #Calcula la energía del sistema
    def energy(self):
        
        (m,MP,l,g,f,b,I,fza)=self.params
        
        K = (0.5*MP*(self.estado[1]**2))+(0.5*m*((self.estado[1]**2)-(2.0*self.estado[1]*l*cos(self.theta())*self.estado[3])+(l**2)*(self.estado[3]**2)))+(0.5*I*(self.estado[3]**2))
        U = -1.0*m*g*l*cos(self.theta())
        
        return K+U
    
    #Ejecuta un paso del tiempo, conocido como dt, y actualiza el estado
    def step(self,dt):
        
        self.estado = odeint(self.dynamics, self.estado, [0,dt])[1]

        self.time_elapsed += dt

    #Resuelve la dinámica en el delta del tiempo dado
    def integrate(self, num_steps=3000, t_i=0, t_f=30):
            
        self.tau = np.linspace(t_i, t_f, num=num_steps, retstep=True)
        
        self.trajectory = odeint(self.dynamics, self.estado_inicial, self.tau)
        #self.trajectory[0,0] = self.x_i
        #self.trajectory[0,1] = self.xprima_i
        #self.trajectory[0,2] = self.theta_i
        #self.trajectory[0,3] = self.thetap_i

        #for j in range (num_steps -1):
            #self.trajectory[j+1] = metodo(self.trajectory[j], self.tau[j], self.dt, self.dynamics)

        
    def plot(self):
        
        fig=plt.fig(figsize=(10,6))
        fig.subtitle("Pendulo Invertido",fontsize=14,fontweight='bold')
        
        ax = a3d.Axes3D(fig,rect=[0,0,0.6,1])
        ax.set_autoscale_on(False)
        ax.set_xlim3d((0,30))
        ax.set_ylim3d((-1,1))
        ax.set_zlim3d((-1,1))
        ax.set_xlabel(r'$t$')
        ax.set_ylabel(r'$x$')
        ax.set_zlabel(r'$y$')
        ax.plot3D(self.tau, self.x(), self.y())

        fig.subplots_adjust(left=0.66,bottom=0.05,top=0.95)

        bx = fig.add_subplot(211)
        bx.set_autoscale_on(True)
        bx.set_ylabel(r'$\theta$')
        bx.set_title('t')
        bx.plot(self.tau,self.theta())
        
        cx = fig.add_subplot(212)
        cx.set_autoscale_on(True)
        cx.set_ylabel(r'$\omega$')
        cx.plot(self.tau,self.omega())

             
        fig, dx = plt.subplots(4,1, figsize = (10,8), sharex=True)

        dx[0].plot(self.tau, self.x(), label="x", color="blue")
        dx[1].plot(self.tau, self.xprima(), label="x prima", color="green")  
        dx[2].plot(self.tau, self.theta(), label="theta", color="blue")
        dx[3].plot(self.tau, self.thetap(), label=" theta prima", color="green")


        dx[0].set_ylabel("x (m)")
        dx[0].set_xlabel("tiempo (s)")

        dx[1].set_ylabel("x prima (m/s)")
        dx[1].set_xlabel("tiempo (s)")

        dx[2].set_ylabel("theta (radianes)")
        dx[2].set_xlabel("tiempo (s)")

        dx[3].set_ylabel("theta prima (rad/s)")
        dx[3].set_xlabel("tiempo (s)")
        
        plt.show()
        
    def xy_snapshot(self):
        plt.figure(1, figsize=(8,6))
        plt.plot(self.x(), self.y())

        plt.show()
        
    #Proceso de animación    
    def animar(self, dt):
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                             xlim=(-2, 2), ylim=(-2, 2))
        ax.grid()

        line, = ax.plot([], [], 'o-', lw=2)
        time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
        energy_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)
        
        def init():
            """Inicia la animación"""
            line.set_data([], [])
            time_text.set_text('')
            energy_text.set_text('')
            return line, time_text, energy_text

        def animate(i):
            """Avanza un paso"""
            self.step(dt)

            line.set_data(*self.position())
            time_text.set_text('time = %.1f' % self.time_elapsed)
            energy_text.set_text('energy = %.3f J' % self.energy())
            return line, time_text, energy_text

        from time import time
        t0 = time()
        animate(0)
        t1 = time()
        interval = 1000 * dt - (t1 - t0)

        ani = animation.FuncAnimation(fig, animate, frames=300,
                                      interval=interval, blit=True, init_func=init)

        return ani
        
       
    #def inicial_condicion(self, x_i, xprima_i,theta_i,thetap_i):
        #self.x_i = x_i
        #self.xprima_i = xprima_i 
        #self.theta_i = theta_i
        #self.thetap_i =thetap_i

   

   