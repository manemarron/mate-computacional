#Tenemos el código:

for k = 1:6
  x = linspace(0, 4*pi, 2^(k+1)+1);
  subplot(2,3,k), plot(x, cos(3*x)-2*sin(x))
  axis([0, 4*pi, -1.5, 1.5])
end

print('segundaGraficaOriginal',"-deps")

#Para cada k=1,...,6 se generará un intervalo x de 0 a 4*pi, donde x 
#se fraccionará en 2^(k+1)+1 subintervalos. Observar que cuando k aumenta, la gráfica se define mejor.
#Asimismo, con el 'subplot' se crean cinco 'áreas gráficas' (dos #renglones, 3 columnas) y para cada k=1,...,6 se activa, de izquierda #a derecha y de arriba a abajo, el área k donde para esa k se imprime #el gráfico correspondiente.
#De otro lado, el 'axis' "acomoda" en el rango precisado [x1,x2,y1,y2] el gráfico #que se imprime, donde [x1,x2] es el dominio que queremos mientras que [y1,y2] es el codominio.

#¿Qué pasa si ahora tenemos 'subplot(3,2,k)'?

for k = 1:6
  x = linspace(0, 4*pi, 2^(k+1)+1);
  subplot(2,3,k), plot(x, cos(3*x)-2*sin(x))
  axis([0, 4*pi, -1.5, 1.5])
end

print('segundaGraficaSubplot',"-deps")

#Ocurre exactamente lo mismo sólo que ahora se acomodan las 6 'áreas #gráficas' en tres renglones y dos columnas.

#Finalmente, ¿qué sucede si retiramos el 'axis'?

for k = 1:6
  x = linspace(0, 4*pi, 2^(k+1)+1);
  subplot(3,2,k), plot(x, cos(3*x)-2*sin(x))
end

print('segundaGraficaAxis',"-deps")

#Las gráficas no se imprimen en un rango 'estándar' sino que el programa 'elige' en qué rango hacerlo respetando el dominio original de x.
