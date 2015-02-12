# se crea un vector de -5 a 5 con 51 divisiones
# se calcula la funcion ((1+x^2)^-1)*sin(x^2)
# se grafica
 
x=linspace(-5,5,51)
y=((1+x.^2).^-1).*sin(x.^2)
plot(x,y)
print('tarea01',"-deps")
print('tarea01',"-dpng")