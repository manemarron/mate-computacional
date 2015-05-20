x = single(77777.0)
y = single(7.0)
inv_y = 1.0 / y

z = x / y
z1 = x * inv_y

if (z != z1)
  sprintf("%1.3f != %1.3f", z, z1)
  sprintf("%1.30f != %1.30f", z, z1)
else
  sprintf("%1.3f == %1.3f", z, z1)
  sprintf("%1.30f == %1.30f", z, z1)
endif
%{
Lo primer que hace es agarrar el valor de los numeros dados en SP.
luego calcula el inverso multiplicativo de y.
entonces x/y "en teoría" debería ser igual a x * inverso multiplicativo de yambas multiplicaciones las mete en z y z1.
Entonces compara si son igual o distintas
Como son distinitas imprime 2 veces(una con 3 y otra con 30 cifras significativas) ambos números y con un signo de distinto entre ellos.
z y z1 son SP, así los interpreta la computadora al ser hechos de SP
}%
