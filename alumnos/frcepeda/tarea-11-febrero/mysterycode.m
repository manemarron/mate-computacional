for k = 1:6
  x = linspace(0, 4*pi, 2^(k+1)+1);
  subplot(2,3,k), plot(x, cos(3*x)-2*sin(x))
  axis([0, 4*pi, -1.5, 1.5])
end

% El código anterior hace 6 gráficas (k) de la misma función,
% pero cada vez dibujando más puntos (aproximadamente 2
% veces más puntos cada vez).

% La función subplot(r,c,i) arregla el entorno para que
% se divida en r filas x c columnas y se prepare para dibujar
% en la iésima casilla de esa matriz. Por lo tanto, si
% se llamara subplot(3,2,k) se dibujarían 3 filas x 2 columnas
% en vez de 2 columnas x 3 filas.

% Si se quitara la instrucción axis, Octave intenta elegir
% los mejores parámetros. En este caso no queremos eso porque
% además de que es muy malo eligiendo los valores, aquí queremos
% ver cómo cambia la gráfica conforme se agregan más puntos,
% por lo que ajustar los ejes automáticamente dependiendo
% de los datos es contraproducente.
