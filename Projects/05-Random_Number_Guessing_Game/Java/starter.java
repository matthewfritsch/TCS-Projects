import java.util.Scanner;
import java.util.Random;
public class starter{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        Random rand = new Random();
        System.out.println("Welcome to my number guessing game!");
        System.out.println("Your random number will exist between 1 and 100");
        System.out.println("You've got 6 guesses, good luck!");
        int choice = 0;
        int number = rand.nextInt(100)+1;
        int guesses = 6;
        while(guesses > 0 && choice != number){
            System.out.println("Make your choice: ");
            choice = scan.nextInt();
            guesses--;
            if(choice > number){
                System.out.println("You guessed too high!");
            }
            else if(choice < number){
                System.out.println("You guessed too low!");
            }
        }
        if(choice == number){
            System.out.println("You got the number!");
        }
        else{
            System.out.println("You ran out of guesses! The number was " + number);
        }
    }
}