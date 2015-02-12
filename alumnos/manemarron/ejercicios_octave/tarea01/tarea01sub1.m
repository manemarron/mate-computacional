# se hace un ciclo 6 veces ya que se harán 6 sub-gráficas
# en cada iteración se declara el vector x de 0 a 4pi, pero con cada iteración aumenta exponencialmente el número de divisiones
# se grafica la función y(x)=cos(3x)-2sin(x)
# se pone el eje X de 0 a 4pi y el eje Y de -1.5 a 1.5

for k = 1:6
  x = linspace(0, 4*pi, 2^(k+1)+1);
  subplot(2,3,k), plot(x, cos(3*x)-2*sin(x))
  axis([0, 4*pi, -1.5, 1.5])
end
print('tarea01sub1',"-dpng")
print('tarea01sub1',"-deps")