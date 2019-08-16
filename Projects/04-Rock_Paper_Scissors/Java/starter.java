import java.util.Random;
import java.util.Scanner;

public class starter{
    public static void main(String[] args){
        System.out.println("Welcome to Rock, Paper, Scissors! Your opponent is the computer!");
        Random random = new Random();
        Scanner s = new Scanner(System.in);
        System.out.println("Type rock, paper, or scissors: ");
        String user = s.next();
        int number = random.nextInt(3)+1;
        String computer = "";
        if( number == 1){
            computer = "rock";
        }
        else if(number == 2){
            computer = "paper";
        }
        else{
            computer = "scissors";
        }

        if( user.equals( computer)){
            System.out.println("It was a tie!");
        }
        else if( user.equals( "rock")){
            if( computer.equals( "paper")){
                System.out.println("You lost, CPU chose paper!");
            }
            else if( computer.equals( "scissors")){
                System.out.println("You won, CPU chose scissors!");
            }
        }
        else if( user.equals( "paper")){
            if( computer.equals( "scissors")){
                System.out.println("You lost, CPU chose scissors!");
            }
            else if( computer.equals( "rock")){
                System.out.println("You won, CPU chose rock!");
            }
        }
        else if( user.equals( "scissors")){
            if( computer.equals( "rock")){
                System.out.println("You lost, CPU chose rock!");
            }
            else if( computer.equals( "paper")){
                System.out.println("You won, CPU chose paper!");
            }
        }
        else{
            System.out.println("That was not an option!");
        }
        s.close();
    }
}