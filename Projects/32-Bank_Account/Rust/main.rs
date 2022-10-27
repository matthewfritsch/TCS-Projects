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

fn input_string() -> String {
    user_input_str().expect("String could not be entered through stdin.")
}

fn user_input_i32() -> Result<i32, ParseIntError> {
    let mut buff = String::new();
    let _rl_result = io::stdin().read_line(&mut buff);
    Ok(buff.trim()
           .parse()?)
}

fn input_int() -> i32 {
    user_input_i32().expect("Integer could not be entered through stdin.")
}

fn flush() {
    io::stdout().flush()
                .expect("stdout ran into an error while flushing.")
}


fn main() {
        
}


