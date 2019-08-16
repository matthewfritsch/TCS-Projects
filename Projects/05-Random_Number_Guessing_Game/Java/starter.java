public class starter{
    public static void main(String[] args){
        System.out.println("Welcome to my number guessing game!");
        System.out.println("Your random number will exist between 1 and 100");
        System.out.println("You've got 6 guesses, good luck!");
        choice = 0;
        number = random.randint(1,100);
        guesses = 6;
        while(guesses > 0 && choice != number){
            choice = int(input("Make your choice: "));
            guesses = guesses-1;
            if(choice > number){
                System.out.println("You guessed too high!");
            }
            else if(choice < number){
                System.out.println("You guessed too low!");
            }
        
            if(choice == number){
                System.out.println("You got the number!");
            }
            else{
                System.out.println("You ran out of guesses! The number was", number);
            }
        }
    }
}