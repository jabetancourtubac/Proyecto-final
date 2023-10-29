package calculadorpromedio;

import java.util.Scanner;

public class CalculadorPromedio {

    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        
        System.out.print("\nIngrese el numero de materias que cursa: ");
        
        int cantidadMaterias = teclado.nextInt();
        
        System.out.print("\nIngrese la cantidad de notas por materia: ");
        
        int cantidadNotas = teclado.nextInt();
        
        double[][] arregloNotas = new double [cantidadMaterias][cantidadNotas];
        
        double promedio;
        
        for (int i = 0; i < arregloNotas.length; i++){
        
            for (int j = 0; j < arregloNotas[i].length; j++){
                
                System.out.print("\nIngrese la nota " + (j + 1) + " de la materia " + (i + 1) + ": ");
            
                arregloNotas[i][j] = teclado.nextDouble();
            
            }
        
        }
        
        for (int i = 0; i < arregloNotas.length; i++){
            
            promedio = 0;
            
            System.out.print("\nMateria " + (i + 1) + ":");
        
            for (int j = 0; j < arregloNotas[i].length; j++){
            
                System.out.print("  " + arregloNotas[i][j]);
                
                promedio += arregloNotas[i][j];
            
            }
            
            if ((promedio / (double)arregloNotas[i].length) > 9.6){
            
                System.out.println("  (aprobada).");
            
            }
            
            else{
            
                System.out.println("  (reprobada).");
                
            }
        
        }
        
    }
    
}
