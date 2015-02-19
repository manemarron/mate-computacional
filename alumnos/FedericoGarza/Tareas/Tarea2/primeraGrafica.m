x=linspace(-5,5,1000)
y=(1./(1+x.**2)).*sin(x.**2)
plot(x,y)
print('primeraGrafica',"-dpng")
