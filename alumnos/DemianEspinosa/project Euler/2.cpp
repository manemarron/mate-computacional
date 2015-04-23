/*
   construyo un arreglo de los números de fibonacci con la fórmula recursiva de sumar los dos anteriores, mientras no exceda el límite
   del problema de los 4000000. Además, siempre que lo calculo, checo si el pasado(que está dentro del rango querido) es par, y si es 
   así, se suma a la respuesta.Finalmente la respuesta es: 46137332
*/

#include <cstdio>

#define MAX 4000000

using namespace std;

int fib[1000];

int main(){
	int i, ans;
	fib[0] = fib[1] = 1;
	for(ans = 0, i = 2; i <= 1000 & fib[i - 1] <= MAX; i++){
		if(fib[i -1] % 2 == 0)
			ans += fib[i - 1];
		fib[i] = fib[i - 2] + fib[i - 1];
	}
	printf("The sum of the even-valued terms of fibonacci that does not exceed 4000000 is: %d\n", ans);
}
