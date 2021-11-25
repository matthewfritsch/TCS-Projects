use std::io;
use std::io::Write;
use rand::Rng;

fn user_input_str() -> String {
    let mut buff = String::new();
    let _rl_result = io::stdin().read_line(&mut buff);
    buff.trim().to_string()
}

fn user_input_i32() -> i32 {
    let mut buff = String::new();
    let _rl_result = io::stdin().read_line(&mut buff);
    let to_ret : i32 = buff.trim().parse().unwrap();
    to_ret
}

fn main() {
    let mut rand_gen = rand::thread_rng();
    
    println!("Welcome to Rock, Paper, Scissors! Your opponent is the computer!");
    print!("Choose 'rock', 'paper', or 'scissors': ");
    io::stdout().flush().unwrap();

    let user = user_input_str();
    let number : u8 = 1 + rand_gen.gen()%3;
    let mut computer : &str;
    if number == 1 {
        computer = "rock";
    }
    else if number == 2 {
        computer = "paper";
    }
    else{
        computer = "scissors";
    }

    if user == computer {
        println!("It was a tie!");
    }
    else if user == "rock" {
        if computer == "paper" {
            println!("You lost, CPU chose paper!");
        }
        else if computer == "scissors" {
            println!("You won, CPU chose scissors!");
        }
    }
    else if user == "paper" {
        if computer == "scissors" {
            println!("You lost, CPU chose scissors!");
        }
    }
    else if computer == "rock" {
        println!("You won, CPU chose rock!");
    }
    else if user == "scissors" {
        if computer == "rock" {
            println!("You lost, CPU chose rock!");
        }
        else if computer == "paper" {
            println!("You won, CPU chose paper!");
        }
    }
    else{
        println!("That was not an option!");
    }
}