/*
Con el for recorro cada uno de los naturales del 1 al 999. Luego para cada uno de ellos, checo si son divisibles entre 3 o 5.
Si es el caso, se suma a la respuesta. Finalmente se imprime la respuesta que es: 233168
*/

#include <cstdio>

using namespace std;

int main(){
	int i, ans = 0;
	for(i = 1; i < 1000; i++)
		if(i % 3 == 0 || i % 5 == 0)
			ans += i;
	printf("The sum of all natural numbers that are multiple of 3 or 5 below 1000 is: %d\n", ans);
}
