
/**
 *
 * @author Javier
 */
public class Euler2 {

    public static int problema6(int n) {
	return (n * (n + 1) / 2) * (n * (n + 1) / 2)	//Aplico fórmulas para calcular suma de números 
		- n * (n + 1) * (2 * n + 1) / 6;	//consecutivos y de números consecutivos
							//elevados al cuadrado
    }

    public static int problema9(int suma) {
	int c = (suma % 2 == 0) ? (suma - 2) / 2 : (suma - 1) / 2;	//calculo c sabiendo que debe ser menor a la mitad de
	for (; c > 0; c--) {						    //la suma a + b + c (a**2 + b**2 = c**2)
									//pruebo cada valor de 'c' posible
	    int a = c - 1;						// a < c; por lo que empiezo asignando a 'a' 'c -1'
	    for (; a > 0; a--) {					//para cada valor de c, pruebo cada valor de a posible
		int b = (int) Math.sqrt(c * c - a * a);			
		if (a + b + c == suma 
			&& a * a + b * b == c * c) {				//si el número b que completaría la terna es entero
		    return a * b * c;					//regresa el producto de a, b y c
		}				    
	    }
	}
	return 0;							//regresa '0' si la suma no puede lograrse con una
    }									    //terna pitagórica

    public static void main(String args[]) {
	System.out.println(problema6(100));
	System.out.println(problema9(1000));
    }
}
