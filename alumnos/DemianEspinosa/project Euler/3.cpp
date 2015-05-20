/*
   Creo una función, que me responde el primo más pequeño de un número. La función checa con cada entero desde el 2 hasta la raiz 
   del número buscan el primero que divida al número. Con esto asegura probar todos los posibles primeros. En caso de no encontrar
   ninguno que lo divida, el número es primo, y la respuesta es el número mismo. Finalmente para dar la respuesta al problema
   se va obteniendo cada primo en orden creciente del número dado. Esto lo hace obteniendo el primo más pequeño, y pregunta ahora
   el primo más pequeño del número actual entre el primo obtenido. Así iterativamente va consiguiendo cada uno de los primos
   hasta llegar a un número que es primo, y será el más grande, finalmente respone ese y es: 6857
*/   

#include <cstdio>
#include <algorithm>


using namespace std;

long long int getFirstPrime(long long int x){
	int i;
	for(i = 2; i * i <= x; i++)
		if(x % i == 0)
			return i;
	return x;
}

long long int N = 600851475143;

int main(){
	while(getFirstPrime(N) != N){
		 N = N / getFirstPrime(N);
	}
	printf("The largest prime of 600851475143 is: %lld\n", N);
}	
