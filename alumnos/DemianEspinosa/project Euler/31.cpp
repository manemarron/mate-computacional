/*
   Lo resolví usando una técnica llamada programación dinámica. Lo que hago es definir una función dp(i,j) que regresa las maneras de formar
   j usando las monedas en un arreglo(yo lo declaro como coins) a partir de la moneda i(en este caso hay 8 monedas). La respuesta al
   problema será por como la definí dp(0, 200) (es apartir de 0 ya que el arreglo está indexado en 0). Lo que hace el código
   es computar todos los estados (que son i * j) usando información ya obtenida antes y partiendo de un caso base. Mi caso base es 
   dp(i,0) = 1, ya que siempre que tengas que representar 0, lo podrás hacer de una manera. a partir de ahí, podemos computar un estado
   cualquiera usando casos anteriores como, si mi estado es usando a partir de i y obtener j, hay de 2 maneras, que use la moneda en i o 
   que no la use. Si la uso son dp(i, j - coins[i]) si no la uso, son dp(i + 1. j). 
*/

#include <cstdio>

using namespace std;

int dp[10][205], coins [10] = {1, 2, 5, 10, 20, 50, 100, 200};

int main(){
	int i, j; 

	for(i = 0; i <= 7; i++)
		dp[i][0] = 1;
	for(i = 7; i >= 0; i--)
		for(j = 1; j <= 200; j++)
			if(coins[i] <= j)
				dp[i][j] = dp[i][j - coins[i]] + dp[i + 1][j];
			else
				dp[i][j] = dp[i + 1][j];
	printf("The number of ways 200 can be made using this value of coins is: %d\n", dp[0][200]);

}
