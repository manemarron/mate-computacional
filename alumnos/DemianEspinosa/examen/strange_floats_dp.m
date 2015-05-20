x = 77777.0
y = 7.0
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
Hace lo mismo que el otro programa, excepto que ahora como no se especificó
el tipo a los números, octave los interpreta como double precision.
Luego, al hacer el cálculo del "inverso multiplicativo de y", puede tener
más precisión en su cálculo. Este hace que al evaluar z1 sí te de el mismo uque z, por lo que termina imprimiendo el caso en que se da la igualdad a 
diferencia del pasado.

z y z1 son DP
}%
