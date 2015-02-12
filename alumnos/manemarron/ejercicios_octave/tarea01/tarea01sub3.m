# se hace un ciclo 6 veces ya que se harán 6 sub-gráficas 
# en cada iteración se declara el vector x de 0 a 4pi, pero con cada iteración aumenta exponencialmente el número de divisiones
# se grafica la función y(x)=cos(3x)-2sin(x)
# al quitar el axis, se quita la configuracion de los ejes

for k = 1:6
  x = linspace(0, 4*pi, 2^(k+1)+1);
  subplot(3,2,k), plot(x, cos(3*x)-2*sin(x))
end
print('tarea01sub3',"-dpng")
print('tarea01sub3',"-deps")