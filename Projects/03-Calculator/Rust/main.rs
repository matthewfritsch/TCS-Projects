use std::io;
use std::io::Write;

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
    println!("Welcome to my basic, two number calculator.");
    
    print!("Type in your first number: ");
    io::stdout().flush().unwrap();
    let number1 = user_input_i32();

    print!("Type in your op: ");
    io::stdout().flush().unwrap();
    let operator = user_input_str();

    print!("Type in your second number: ");
    io::stdout().flush().unwrap();
    let number2 = user_input_i32();

    if operator == "+" {
        println!("{}", add(number1, number2));
    }
    else if operator == "-" {
        println!("{}", sub(number1, number2));
    }
    else if operator == "*" {
        println!("{}", mul(number1, number2));
    }
    else if operator == "/" {
        println!("{}", div(number1, number2));
    }
    else{
        println!("That was not an operator we have!");
    }

    
}

fn add(a : i32, b : i32) -> i32 {
    a+b
}
fn sub(a : i32, b : i32) -> i32 {
    a-b
}
fn mul(a : i32, b : i32) -> i32 {
    a*b
}
fn div(a : i32, b : i32) -> i32 {
    a/b
}