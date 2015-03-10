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
