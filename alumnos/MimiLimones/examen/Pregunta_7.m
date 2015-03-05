
# Programa 1
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

# Lo que el código anterior realiza es que va rezagando los decimales, y cuando comparamos a z contra
#z1, lo que tenemos es que z1 tiene más decimales que z. Lo cual genera que cuando los comparamos, 
# al final de cuentas no son iguales. 
# Tenemos que el z es un SP y el z1 es un DP. 

# Programa 2

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

# Tenemos que en este caso, ambos resultados son iguales en las dos operaciones, y eso ocurre al momento
# de definir a ambos, z y z1, ya que en este caso no especificamos que ambos tendrían que ser singles.
# Por lo tanto, nos dan números con decimales iguales. 
# Tenemos que los dos números son SP.

