
/**
 *
 * @author Javier
 */
import java.util.LinkedList;

public class Euler1 {

    //método que resuelve el primer problema
    public static int problema1(int n) {
	int a = (n - 1) / 3;		//cuento cuántos múltiplos de 3 hay antes de n
	int suma = a * (a + 1) / 2 * 3;	//sumo esos de múltiplos de 3
	a = (n - 1) / 5;		//cuento cuántos múltiplos de 5 hay...
	suma += a * (a + 1) / 2 * 5;	//sumo esos múltiplos de 5
	a = (n - 1) / 15;		//cuento cuántos múltiplos de 15 hay...
	suma -= a * (a + 1) / 2 * 15;	//resto esos múltiplos de 15 pues los sumé dos veces 
	return suma;
    }

    //método que resuelve el segundo problema
    public static int problema2(int n) {
	int a = 1;				//variable que empieza en 1 por ser el primer término de la serie
	int b = 2;				//variable que empieza en 2 por ese el segundo término de la serie
	int temp;				//variable temporal
	int suma = 0;				//varaible que lleva la suma que pide le problema

	while (suma < n) {	//ciclo que termina cuando la suma sea mayor que n, 4,000,000
	    suma += (b % 2 == 0) ? b : 0;	//si el término es par es agregado a la suma
	    temp = a;
	    a = b;				//se recorre la serie
	    b = temp + a;			//se calcula el valor del siguiente término sumando los dos anteriores
	}
	return suma;
    }

    // método calcula el máximo común divisor utilizando el algoritmo de Euclides
    public static long mcd(long m, long n) {
	if (m == 0) {			
	    return n;
	}
	return (mcd(n % m, m));
    }

    //método que obtiene una lista de primos menores a n
    private static LinkedList<Long> obtenPrimos(long n, LinkedList<Long> primos) {
	primero:				//etiqueta del primer ciclo
	for (long i = 2; i <= n; i++) {		
	    if (!primos.contains(i)) {		//si la lista de primos no contiene i
		for (long x : primos) {		//para cada primo en la lista:
		    if (mcd(x, i) != 1) {	//verifica que su mcd sea igual de 1
			continue primero;	//en caso de ser diferente, significa que es número compuesto, por lo
		    }				    //que el primer ciclo avanza a la siguiente iteración
		}
		primos.addFirst(i);		//si mcd fue igual a 1 para cada número que ya estaba en la lista,
	    }					    //significa que el número es primo, por lo que se agrega a la lista
	    if (n % i == 0) {			//si puede dividir entre i, lo divide 
		return obtenPrimos(n / i, primos);
	    }
	}
	return primos;
    }

    //método que resuelve el problema 3
    public static long problema3(long n) {
	LinkedList<Long> primos = obtenPrimos(n, new LinkedList<Long>());   //obtiene una lista de primos menores a n
	for (long x : primos) {						    //para cada primo en la lista:
	    if (n % x == 0) {						    //prueba si es divisor de n
		return x;						    //si sí, regresa ese primo
	    }								    //(la lista tiene orden inverso)
	}
	return 1;							    //si ninguno lo dividió, regresa 1
    }

    public static void main(String args[]) {
	System.out.println("Problema 1: " + problema1(1000));
	System.out.println("Problema 2: " + problema2(4000000));
	System.out.println("Problema 3: " + problema3(600851475143L));
    }
}
