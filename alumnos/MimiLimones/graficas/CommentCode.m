for k = 1:6
  x = linspace(0, 4*pi, 2^(k+1)+1);
  subplot(3,2,k), plot(x, cos(3*x)-2*sin(x))
  axis([0, 4*pi, -1.5, 1.5])
end

# El código genera 6 gráficas diferentes, las cuales representan la misma
# función, pero cada vez se va suavizando más la gráfica, esto debido a 
# que los espacios entre los puntos se van disminuyendo. 

# Si hacemos el cambio dentro del subplot, la gráfica se ensancha y se reduce
# su altura. Esto debido al tamaño en el cual el subplot ajusta la gráfica. 

# Si se quita el comando axis, la gráfica se dibuja hasta el mayor valor
# que se tiene en ésta y corta la gráfica. No respeta un mismo valor de
# margen como cuando se pone el axis. 