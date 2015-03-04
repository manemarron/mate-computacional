#no me queda claro si es que teniamos que reutilizar los valores de la diagonal
#use 2 formas en las que podía obtener una matriz con la diagonal indicada
ej1aa=np.linspace(0.25,5.25,25)
forma=np.reshape(ej1aa, (5,5))
ej1a = np.round(forma)
print ej1a
ej1_a=np.ones((5,5))
for j in range(1, 5):
    ej1_a[j,j]=j+1.0
ej1_a,1
