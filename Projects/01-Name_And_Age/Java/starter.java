import java.util.Scanner;

public class starter{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        System.out.print("Please type in your name: ");
        String name = s.nextLine();
        System.out.print("Please type in your age: ");
        int age = s.nextInt();

        System.out.println(name + " is " + age + " years old");

        String name2 = "Peter Parker";
        int age2 = 17;

        System.out.println(name2 + " is " + age2 + " years old");

        if(age > age2){
            System.out.println(name + " is older than " + name2);
        }
        else if(age < age2){
            System.out.println(name + " is younger than " + name2);
        }
        else{
            System.out.println(name + " is the same age as " + name2);
        }
        s.close();
    }
}