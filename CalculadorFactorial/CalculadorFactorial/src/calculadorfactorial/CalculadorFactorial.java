package calculadorfactorial;

import java.util.Scanner;

public class CalculadorFactorial {

    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        
        System.out.print("\nIngrese un numero entero: ");
        
        int numero = teclado.nextInt();
        
        int copia = numero;
        
        int factorial = 1;
        
        while (numero != 1){
        
            factorial = numero * factorial;
                    
            numero -= 1;
        
        }
        
        System.out.println("\nEl factorial de " + copia + " es " + factorial + ".");
        
    }
    
}
