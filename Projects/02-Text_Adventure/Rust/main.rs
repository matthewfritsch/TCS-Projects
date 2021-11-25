use std::io;
use std::io::Write;

fn user_input_str() -> String {
    let mut buff = String::new();
    let _rl_result = io::stdin().read_line(&mut buff);
    buff.trim().to_string()
}

// fn user_input_i32() -> i32 {
//     let mut buff = String::new();
//     let _rl_result = io::stdin().read_line(&mut buff);
//     let to_ret : i32 = buff.trim().parse().unwrap();
//     to_ret
// }

fn main() {
    println!("You wake up in a forest, with no other signs of human life in sight. You don't remember arriving here, and do not recognize where you are.");
    println!("You're right on top of a trail, which leads three different ways that you must choose from:");
    println!("1. Enter the nearby cave");
    println!("2. Follow the dirt trail over a hill");
    println!("3. Walk deeper into the forest.");
    print!("Type choice here (1,2,3): ");
    io::stdout().flush().unwrap();
    let mut choice = user_input_str();

    while !(choice == "1" || choice == "2" || choice == "3") {
        print!("That is not a choice, please try 1, 2, or 3: ");
        choice = user_input_str();
    }

    if choice == "1" {
        println!("You enter the cave, to find a bear is comfortably laying down, its head on its hands.");
        println!("Instinctually, you choose to:");
        println!("1. Attack the bear");
        println!("2. Sneak past the bear");
        println!("3. Try to befriend the bear");
        print!("Please type the number for your choice: ");
        io::stdout().flush().unwrap();
        choice = user_input_str();

        while !(choice == "1" || choice == "2" || choice == "3") {
            print!("That is not a choice, please try 1, 2, or 3: ");
            io::stdout().flush().unwrap();
            choice = user_input_str();
        }

        if choice == "1" { 
            println!("What were you thinking? You can't fight a bear! You were eaten!");
        }
        else if choice == "2" {
            println!("The bear is definitely not asleep, it sees you tiptoeing around, gets up, and attacks! You were eaten!");
        }
        else if choice == "3" {
            println!("The bear, eerily enough, seems quite docile. He starts walking out of the cave with you, and directs you all the way back home!");
        }
    }
    else if choice == "2" {
        println!("You follow the dirt trail, which leads you over top a small yet, steep hill. Behind the hill is a horse, which appears to be waiting for you.");
        println!("Instinctually, you choose to:");
        println!("1. Feed the horse");
        println!("2. Ride the horse");
        println!("3. Leave the hill");
        print!("Please type the number for your choice: ");
        io::stdout().flush().unwrap();
        choice = user_input_str();

        while !(choice == "1" || choice == "2" || choice == "3") {
            print!("That is not a choice, please try 1, 2, or 3: ");
            io::stdout().flush().unwrap();
            choice = user_input_str();
        }

        if choice == "1" {
            println!("The horse was not waiting to be fed, so it gets spooked and kicks you! You're knocked out!");
        }
        else if choice == "2" {
            println!("The horse was waiting for you to hop on, and as you did, it ran you straight to your home!");
        }
        else if choice == "3" {
            println!("You leave the hill and, along the way, lose track of where you are. You get so lost that you never seem to make it out of the forest.");
        }
    }
    else if choice == "3" {
        println!("You walk deeper into the forest, and see some people who are all around a bonfire, staring right into it.");
        println!("Instinctually, you choose to:");
        println!("1. Attack the people");
        println!("2. Talk to the people");
        println!("3. Run away from the people");
        print!("Please type the number for your choice: ");
        io::stdout().flush().unwrap();
        choice = user_input_str();

        while !(choice == "1" || choice == "2" || choice == "3") {
            print!("That is not a choice, please try 1, 2, or 3: ");
            io::stdout().flush().unwrap();
            choice = user_input_str();
        }
        if choice == "1" {
            println!("There are so many people here, and they all attack you right back at the same time. You fall unconscious!");
        }
        else if choice == "2" {
            println!("As a person sees you approaching, they all begin screaming and chasing you. They were too fast, and you fall unconscious!");
        }
        else if choice == "3" {
            println!("You understood that these people were kind of scary, and when you begin running away you start to recognize where you are! You make it out of the forest back to your home!");
        }
    }
}