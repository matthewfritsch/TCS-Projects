import java.util.Scanner;

public class starter{
    public static void main(String[] args){
        System.out.println("Welcome to my basic, two number calculator.");
        Scanner s = new Scanner(System.in);
        System.out.println("Type in your first number: ");
        int number1 = s.nextInt();
        System.out.println("Type in your op: ");
        String op = s.next();
        System.out.println("Type in your second number: ");
        int number2 = s.nextInt();

        if(op.equals("+")){
            System.out.println(add(number1, number2));
        }
        else if(op.equals("-")){
            System.out.println(subtract(number1, number2) );
        }
        else if(op.equals("*")){
            System.out.println(multiply(number1, number2) );
        }
        else if(op.equals("/")){
            System.out.println(divide(number1, number2) );
        }
        else{
            System.out.println("That was not an operator we have!" );
        }
    }
    public static int add(int a, int b){
        return a+b;
    }
    public static int subtract(int a, int b){
        return a-b;
    }
    public static int multiply(int a, int b){
        return a*b;
    }
    public static double divide(int a, int b){
        return (double)a/(double)b;
    }
}