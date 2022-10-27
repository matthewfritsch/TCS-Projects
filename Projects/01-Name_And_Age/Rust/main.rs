use std::io;
use std::io::Write;
use std::num::ParseIntError;

fn user_input_str() -> Result<String, io::Error> {
    let mut buff = String::new();
    let _rl_result = io::stdin().read_line(&mut buff);
    Ok(buff
        .trim()
        .to_string())
}

fn user_input_i32() -> Result<i32, ParseIntError> {
    let mut buff = String::new();
    let _rl_result = io::stdin().read_line(&mut buff);
    Ok(buff.trim()
           .parse()?)
}

fn flush() {
    io::stdout().flush()
                .expect("stdout ran into an error while flushing.")
}

fn main() {
    print!("Please enter your name: ");
    flush();
    let name = user_input_str().expect("String could not be acquired from stdin.");

    print!("Please enter your age: ");
    flush();
    let age = user_input_i32().expect("Integer could not be acquired from stdin.");

    let name2 = "Peter Parker";
    let age2 = 17;

    if age > age2 {
        println!("{} is older than {}.", name, name2);
    }
    else if age < age2 {
        println!("{} is younger than {}.", name, name2);
    }
    else {
        println!("{} is the same age as {}.", name, name2);
    }
}
