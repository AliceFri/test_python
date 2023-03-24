fn main() {
    println!("Hello, world!");
    let mut x = 5;

    println!("The Value of x is {}", x);
    x = 6;
    println!("The Value of x is {}", x);

    // 遮蔽
    let x = 5;
    let x = x + 1;
    {
        let x = x * 2;
        println!("The Value of x is {}", x);
    }
    println!("The Value of x is {}", x);
}
