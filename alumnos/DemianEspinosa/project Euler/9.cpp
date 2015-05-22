#include <cstdio>

using namespace std;

int a, b, c;

int main(){
	bool flag = false;
	for(a = 1; a <= 332 && !flag; a++)
		for(b = a + 1; 1000 - a - b > b; b++)
			if(a * a + b * b == (1000 - a - b) * (1000 - a - b)){
				printf("The product of abc is: %d\n", a * b * (1000 - a - b));
			}
}
				
			
