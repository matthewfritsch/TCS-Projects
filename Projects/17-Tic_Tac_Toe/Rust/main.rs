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
        
}


