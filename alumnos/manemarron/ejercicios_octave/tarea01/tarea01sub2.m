# se hace un ciclo 6 veces ya que se harán 6 sub-gráficas (al cambiar el 2,3 por 3,2 cambia de tener 2 filas y 3 columnas a tener 3 filas y 2 columnas)
# en cada iteración se declara el vector x de 0 a 4pi, pero con cada iteración aumenta exponencialmente el número de divisiones
# se grafica la función y(x)=cos(3x)-2sin(x)
# se pone el eje X de 0 a 4pi y el eje Y de -1.5 a 1.5

for k = 1:6
  x = linspace(0, 4*pi, 2^(k+1)+1);
  subplot(3,2,k), plot(x, cos(3*x)-2*sin(x))
  axis([0, 4*pi, -1.5, 1.5])
end
print('tarea01sub2',"-dpng")
print('tarea01sub2',"-deps")