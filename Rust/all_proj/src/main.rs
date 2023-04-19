// https://rustwiki.org/zh-CN/rust-by-example/macros/variadics.html
fn main() {
    println!("Hello, world!!!!");
    // data_type();
    // variable_();
    //
    // str_();
    // if_();
    // loop_();
    fn_();
}


fn data_type() {
    // let 变量 = 值
    let food = "黄焖鸡";
    let price = 366;
    let checked = true;

    println!("food is {}", food);
    println!("price is {}", price);
    println!("checked is {}", checked);
}


fn variable_() {

    let name= "peng";
    let name:&str = "quan";     // 变量覆盖
    let mut price = 100;
    price = 200;
    println!("{},  {}", name, price);

    const PI: f64 = 3.14;       // 常量必须声明 类型
    println!("{}", PI);

    static BOOK:&'static str = "一本书";              // static  and  static mut
    println!("{}", BOOK)
}

fn str_() {

    // 字符窗 &str  std::str   字符串 slice 字符串字面量    创建后会一直保存到程序结束
    let lesson = "学习Rust";

    // String Object  堆中， 长度可变
    let s1: String = String::new();
    println!("s1: {}, s1-len: {}", s1, s1.len());
    let s2: String = String::from("hello world");
    println!("s1: {}, s1-len: {}", s2, s2.len());

    let mut s3: String = String::new();
    s3.push_str("push___");
    println!("{}", s3);
    s3.push('O');
    s3.push('O');
    s3.push('K');
    println!("{}", s3);
    let s4 = s3.replace("O", "I");
    println!("{}, {}", s3, s4);
    println!("{}", s3.to_string());

    show_name(s3.as_str());

    let s9 = s3.trim();
    for item in s9.split('O'){
        println!("split: --- {}", item);
    }

    for c in s9.chars(){
        println!("字符： {}", c);
    }

    let A = "A".to_string();
    let B = "B".to_string();

    println!("{}", A + &B);
    // println!("{}", A);

}

fn show_name(name:&str){
    println!("----- {}", name);
}


fn if_(){
    let total = 66;

    if total >= 500 {
        println!("大于 500！！");
    }else if total >= 550 {
        println!("大于 550-");
    }else{
        println!("Other");
    }

    let code="10086";
    let choose = match code {
        "10086"=>"联通",
        "10010"=>"移动",
        _=>"Unknown"
    };
    println!("{}", choose);
}


fn loop_() {
    for num in 1..5{    // 左闭右开     1..=5
        println!("num is {}", num);
    }

    let studyList = vec!["语文", "数学", "物理", "化学"];
    for name in studyList.iter(){   // iter() 每次迭代是借用集合中的一个元素
        println!("learn {}", name);
    }
    for name in studyList.into_iter(){   // iter() 每次迭代是使用集合中的数据，迭代结束后， 集合不可用
        println!("learn {}", name);
    }

    let mut studyList = vec!["语文", "数学", "物理", "化学"];
    for name in studyList.iter_mut(){   // iter() 迭代中可以改变内部元素
        *name = "Nothing";
        println!("learn {}", name);
    }
    println!("{:?}", studyList);

    let mut num = 1;
    while num < 5{
        println!("nums is {}", num);
        num += 1;
    }
}


// 函数，  无明确返回值， 会返回一个单元类型
fn fn_(){
    hello();
    println!("{}", get_name());
    println!("{}", get_name2());

    let mut price = 100;
    double_price(price);
    println!("外部的price {}", price);

    let mut price = 100;
    double_price2(&mut price);
    println!("外部的price {}", price);

    let name = String::from("Bob");
    // show_name(&name);
    // show(&name);
    // println!("调用showname之后的 {}", name)
}

fn hello(){
    println!("Hello Rust");
}

fn get_name() -> String{
    return String::from("hello bob!");
}

fn get_name2() -> String{
    return String::from("hello bob!");
}

fn double_price(mut p: i32) {  // 值传递， 函数内部会创建一个新的值
    p = p * 2;
    println!("内部的 price 是 {}", p);
}

fn double_price2(price: &mut i32) {
    *price = *price * 2;
    println!("内部的 price 是 {}", price);
}

fn show(name: String){
    // show noting
}