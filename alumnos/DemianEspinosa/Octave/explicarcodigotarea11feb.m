for k = 1:6
  x = linspace(0, 4*pi, 2^(k+1)+1);
  subplot(2,3,k), plot(x, cos(3*x) - 2*sin(x))
  axis([0, 4*pi, -1.5, 1.5])
end

%{
El codigo original, por el contador que tiene, graficará 6 gráficas
Pero, por el subplot, se generó una cuadrócula de 2 filas con 3 columnas
donde irán las 6 gráficas.
Además, por la construcción del vector x, lo que cambia en cada gráfica es
que se consideran 2^(k+1)+1 puntos, por lo que cada vez es una gráfica más
precisa.

Cuando se cambia el subplot, ahora en vez der ser una cuadrícula de 2 filas
por 3 columnas, será una cuadrícula de 3 filas, con 2 columnas, donde irán
las 6 gráficas.

Para cuando se quita el axis, lo que hacía era definir los parámetros
de los ejes donde se iba a graficar, sin este, octave da
por automático ciertos ejes de acuerdo a la función. 
%}
