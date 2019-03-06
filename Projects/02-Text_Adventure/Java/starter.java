import java.util.Scanner;

public class starter{
    public static void main(String[] args){
        System.out.println("You wake up in a forest, with no other signs of human life in sight. You don't remember arriving here, and do not recognize where you are.");
        System.out.println("You're right on top of a trail, which leads three different ways that you must choose from:");
        System.out.println("1. Enter the nearby cave");
        System.out.println("2. Follow the dirt trail over a hill");
        System.out.println("3. Walk deeper into the forest.");
        System.out.println("Type choice here (1,2,3): ");
        Scanner s = new Scanner(System.in);
        String choice = s.next();
        while(!(choice.equals("1") || choice.equals("2") || choice.equals("3"))){
            System.out.println("That is not a choice, please try 1, 2, or 3: ");
            choice = s.next();
        }

        if (choice.equals("1")){
            System.out.println("You enter the cave, to find a bear is comfortably laying down, its head on its hands.");
            System.out.println("Instinctually, you choose to:");
            System.out.println("1. Attack the bear");
            System.out.println("2. Sneak past the bear");
            System.out.println("3. Try to befriend the bear");
            System.out.println("Please type the number for your choice: ");
            choice = s.next();

            while(!(choice.equals("1") || choice.equals("2") || choice.equals("3"))){
                System.out.println("That is not a choice, please try 1, 2, or 3: ");
                choice = s.next();
            }

            if (choice.equals("1")){
                System.out.println("What were you thinking? You can't fight a bear! You were eaten!");
            }
            else if(choice.equals("2")){
                System.out.println("The bear is definitely not asleep, it sees you tiptoeing around, gets up, and attacks! You were eaten!");
            }
            else if(choice.equals("3")){
                System.out.println("The bear, eerily enough, seems quite docile. He starts walking out of the cave with you, and directs you all the way back home!");
            }
        }
        else if(choice.equals("2")){
            System.out.println("You follow the dirt trail, which leads you over top a small yet, steep hill. Behind the hill is a horse, which appears to be waiting for you.");
            System.out.println("Instinctually, you choose to:");
            System.out.println("1. Feed the horse");
            System.out.println("2. Ride the horse");
            System.out.println("3. Leave the hill");
            System.out.println("Please type the number for your choice: ");
            choice = s.next();
            while(!(choice.equals("1") || choice.equals("2") || choice.equals("3"))){
                System.out.println("That is not a choice, please try 1, 2, or 3: ");
                choice = s.next();
            }

            if (choice.equals("1")){
                System.out.println("The horse was not waiting to be fed, so it gets spooked and kicks you! You're knocked out!");
            }
            else if(choice.equals("2")){
                System.out.println("The horse was waiting for you to hop on, and as you did, it ran you straight to your home!");
            }
            else if(choice.equals("3")){
                System.out.println("You leave the hill and, along the way, lose track of where you are. You get so lost that you never seem to make it out of the forest.");
            }
        }
        else if(choice.equals("3")){
            System.out.println("You walk deeper into the forest, and see some people who are all around a bonfire, staring right into it.");
            System.out.println("Instinctually, you choose to:");
            System.out.println("1. Attack the people");
            System.out.println("2. Talk to the people");
            System.out.println("3. Run away from the people");
            System.out.println("Please type the number for your choice: ");
            choice = s.next();
            while(!(choice.equals("1") || choice.equals("2") || choice.equals("3"))){
                System.out.println("That is not a choice, please try 1, 2, or 3: ");
                choice = s.next();
            }
            if (choice.equals("1")){
                System.out.println("There are so many people here, and they all attack you right back at the same time. You fall unconscious!");
            }
            else if(choice.equals("2")){
                System.out.println("As a person sees you approaching, they all begin screaming and chasing you. They were too fast, and you fall unconscious!");
            }
            else if(choice.equals("3")){
                System.out.println("You understood that these people were kind of scary, and when you begin running away you start to recognize where you are! You make it out of the forest back to your home!");
            }
        }
        
    }
}