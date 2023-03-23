use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!");


    let aim_number = rand::thread_rng().gen_range(1..101);

    loop {
        println!("Please input your guess. {}", aim_number);
        let mut guess = String::new();  // 可变
        io::stdin().read_line(&mut guess).expect("Failed to read line");
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        match guess.cmp(&aim_number) {
            Ordering::Less => println!("Too Small!"),
            Ordering::Greater => println!("Too Big!"),
            Ordering::Equal => {
                println!("Your Win!");
                break;
            }
        }
    }
}
