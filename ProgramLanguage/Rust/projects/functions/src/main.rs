fn main() {
    println!("Hello, world!");
    another_function(20);
}

// function 带参数
fn another_function(x: i8) {
    println!("The Value of x is {}", x)
}

// 带有返回值的函数，使用表达式 作为 返回值
fn five() -> i32 {
    5
}