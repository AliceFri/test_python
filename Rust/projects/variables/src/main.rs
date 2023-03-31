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


    // 所有权
    println!(" ---------- begin 所有权");
    let mut s = String::from("hello");
    s.push_str(", world!");
    println!("{}", s);

    // 浅拷贝， 移动
    // let s2 = s;
    // println!("{}", s)
    // 只在 栈上的 数据， 是 深拷贝
    let x = 5;
    let y = x;
    println!("x = {}, y = {}", x, y);

    println!(" ---------- begin 所有权 与 函数");
    let s = String::from("hello");  // s 进入作用域
    takes_ownership(s);             // s 的值移动到函数里 ...
    // println!("{}", s);              // ... 所以到这里不再有
    let x = 5;                      // x 进入作用域
    makes_copy(x);                  // x 应该移动函数里，
                                  // 但 i32 是 Copy 的，所以在后面可继续使用 x
}


fn takes_ownership(some_string: String) { // some_string 进入作用域
  println!("{}", some_string);
} // 这里，some_string 移出作用域并调用 `drop` 方法。占用的内存被释放

fn makes_copy(some_integer: i32) { // some_integer 进入作用域
  println!("{}", some_integer);
} // 这里，some_integer 移出作用域。不会有特殊操作