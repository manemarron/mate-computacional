/*
   Es conocido que la suma de los primeros n cuadrados es (n*(n+1)*(2n+1))/6 y que la suma de los primeros números es (n*(n+1)/2, usando
   eso es solo imprimir esa diferencia con n = 100
*/

#include <cstdio>

using namespace std;

int main(){
	printf("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is: %d\n", (100 * 101 / 2) * (100 * 101 / 2) - (100 * 101 * 201 / 6));
}
