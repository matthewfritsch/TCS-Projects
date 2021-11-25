use std::io;
use std::io::Write;

fn main() {
    let mut name = String::new();
    print!("Please enter your name: ");
    io::stdout().flush().unwrap();
    let _nrl = io::stdin().read_line(&mut name);
    name = name.trim().to_string();

    let mut buff = String::new();
    print!("Please enter your age: ");
    io::stdout().flush().unwrap();
    let _arl = io::stdin().read_line(&mut buff);
    let age : u8 = buff.trim().parse().unwrap();

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