/*
   count[i] cuenta el número de letras que tiene el número i. La base del problema consiste en ver los números que te forman los demás.
   Estos son los primeros 19, y las siguientes 8 decenas. Estas las calculo manualmente y las meto en un arreglo. Luego para cada uno
   de los números, checo en qué caso cae, si es menor a 21, ya lo tengo hecho por lo que sólo lo sumo. Si está entre 21 y 99, le sumo
   el número de letras de su decena más el número de letras de su unidad. si está entre 100 y 999, le sumo el número con el que inicia
   el número de letras del hundred, el número de letras del andd en caso de que sea múltiplo de 100, y el número de letras de sus decenas
   y unidades que ha habían sido calculada antes. finalmente agrego las letras de que fuera 1000.
*/

#include <cstdio>

using namespace std;

int count[1000] = {0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8, 6};

int main(){
	int i, andd, hundred, thousand, ans;
	andd = 3;
	hundred = 7;
	thousand = 8;
        count[30] = 6;
	count[40] = 5;
	count[50] = 5;
	count[60] = 5;
	count[70] = 7;
	count[80] = 6;
	count[90] = 6;

	for(i = 1, ans = 0; i <= 1000; i++){
		if( i <= 20)
			ans += count[i];
		else
			if(i < 100)
				ans += count[i] =  count[i - (i % 10)] + count[i % 10];
			else
				if(i < 1000)
					ans += count[i /100] + hundred + (i % 100 == 0 ? 0 : andd) + count[i % 100];
				else
					ans += count[1] + thousand;
	}
	printf("if all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, the number of letters would be: %d\n", ans);
}
