
/**
 *
 * @author Javier
 */
public class Euler3 {

    public static int problema17() {
	String[] unidades = {"one", "two", "three",
	    "four", "five", "six", "seven", "eight", "nine"};
	String[] decenas_sin_diez = {"twenty", "thirty", "forty", "fifty", //no incluyo el 10 porque sólo aparece
	    "sixty", "seventy", "eighty", "ninety"};				    //una vez por cada centena
	String[] entre_diez_y_veinte = {"ten", "eleven", "twelve", "thirteen", //estos números aparece una vez por cada centena
	    "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
	    "nineteen"};

	int cuenta = 0;
	for (String num : unidades) {						    //cuento cuántas veces aparece
	    cuenta += num.length() * 200;					    //cada elemento de unidades[]
//	   cuenta += num.length() * (1000 / 10) * 1;
//	   cuenta += num.length() * 1 * 100;
	}

	for (String num : entre_diez_y_veinte) {					    //estos elementos aparecen una sola
	    cuenta += num.length() * (1000 / 100) * 1;				    //vez por centena
	}

	for (String num : decenas_sin_diez) {					    //estos elementos aparecen diez veces
	    cuenta += num.length() * (1000 / 100) * 10;				    //por centena
	}

	cuenta += (999 - 100 + 1) * "hundred".length();
	cuenta += ((999 - 100 + 1) - 9) * "and".length();
	cuenta += "onethousand".length();
	return cuenta;
    }

    public static int problema31() {
	int centavos = 200;
	int cuenta = 0;

	for (int doscientos = centavos; doscientos >= 0; doscientos -= 200) {	    //en cada ciclo interior de esta búqueda bruta
	    for (int cien = doscientos; cien >= 0; cien -= 100) {		    //se considera qué pasaría si la moneda se 
		for (int cincuenta = cien; cincuenta >= 0; cincuenta -= 50) {	    //degradara a monedas de valor inferior;
		    for (int veinte = cincuenta; veinte >= 0; veinte -= 20) {	    //el caso con unos ya no se hace porque la 
			for (int diez = veinte; diez >= 0; diez -= 10) {	    //moneda de un centavo ya no puede degradarse más.
			    for (int cinco = diez; cinco >= 0; cinco -= 5) {
				for (int dos = cinco; dos >= 0; dos -= 2) {
				    cuenta++;
				}
			    }
			}
		    }
		}
	    }
	}
	return cuenta;
    }

    public static void main(String[] args) {
	System.out.println(problema17());
	System.out.println(problema31());
    }
}
