""
go build <filename>
go run <file>

Go 是静态类型语言， 编译时，编译器会检查变量的类型，所以要求所有的变量都要有明确的类型。

Go 变量/常量只能声明一次，声明多次，编译就会报错

Go 双引号和单引号是不一样的，双引号表示字符串， 单引号表示(rune类型, byte类型的)字符

Go 匿名变量：
    _   不分配内存， 不需要命名, 运行多次声明

Go语言里，浮点数的相关部分只能由10进制表示法表示，而不能由8进制表示法或16进制表示法表示。

Go 语言的 string 是用 uft-8 进行编码的，英文字母占用一个字节，而中文字母占用 3个字节，所以 hello,中国 的长度为 5+1+（3＊2)= 12个字节。

Go 字典的key为不可变对象（除切片，字典，函数之外的内建类型都算）  （python是 数组不算，方法算） （Go map需指定key,value 类型）
""

### 0. fmt
    %b    表示为二进制
    %c    该值对应的unicode码值
    %d    表示为十进制
    %o    表示为八进制
    %q    该值对应的单引号括起来的go语法字符字面值，必要时会采用安全的转义表示
    %x    表示为十六进制，使用a-f
    %X    表示为十六进制，使用A-F
    %U    表示为Unicode格式：U+1234，等价于"U+%04X"
    %E    用科学计数法表示
    %f    用浮点数表示

### 1. 创建变量的方法

    a. 一行声明一个变量         var <name> <type>       
        eg:     var name string = "hello world"
                var name = "hello world"        # 简化
                var rate float32 = 0.89         # 不指定类型时，会被声明为float64
    
    b. 多个变量一起声明
        var (
            name string
            age int
            gender string
        )
    c. 推导声明写法
        var name:= "hello world"
    d. 一行声明多个变量
        name1, age1 := "zhangsan", 14
    e. new函数声明一个指针变量
        ptr := new(int)
        fmt.Println("ptr address: ", ptr)
        fmt.Println("ptr value: ", *ptr)  // * 后面接指针变量，表示从内存地址中取出值
        
### 2. 数据类型， 整型与浮点型
    type    bit         byte            remark
    int     32/64       4/8             与计算机系统的位数有关
    int8    8           1
    int16   16          2
    int32   32          4
    int64   64          8
    
    uint    32/64       4/8                 与计算机系统的位数有关
    uint8   8           1
    uint16  16          2
    uint32  32          4
    uint64  64          8

    2进制 0b/0B       num01:= 0b1100
    8进制 0o/0O
    16进制    0x

    浮点型：
        float32: 1bit符号 8bit指数  23bit尾数
        float64: 1bit符号 11bit指数 52bit尾数
        数值很大，但精度有限， float32 ==> 科学计数法，小数点后6位， float64==> 科学计数法，小数点后15位

### 3. 数据类型 byte rune 与字符串
    
    byte: 占用1个byte, 8个bit, 表示范围在 0 -> 255, 表示的是一个ASCII字符
    eg： var b byte = 65
        var a byte = 'A'

    rune: 占用4个byte, 32个bit, 表示的是一个Unicode字符
    eg: var name rune = '中'


    string:
        string 的本质，其实是一个 byte数组
        而使用反引号，就方便多了，所见即所得，这种叫原生型表示法
        var mystr01 string = "\\r\\n"       var mystr02 string = `\r\n`

### 4. 数据类型: 数组与切片
    数组: 一个由固定长度的特定类型元素组成的序列，一个数组可以由零个或多个元素组成。因为数组的长度是固定的，所以在Go语言中很少直接使用数组。
    
    var arr [3]int
    arr[0] = 1
    arr[1] = 2
    arr[2] = 3
    
    var arr [3]int = [3]int{1， 2， 3}
    arr := [3]int{1, 2, 3}
    arr := [...]int{1,  2, 3}       arr:=[4]int{2:3}    [0, 0, 3, 0]

    [3]int 和 [4]int 虽然都是数组，但他们却是不同的类型，使用 fmt 的 %T 可以查得。

    切片: 切片是对数组的一个连续片段的引用，所以切片是一个引用类型（与python不同，python的切片是新数组）同样是左闭右开

        // 【第一种】
        // 1 表示从索引1开始，直到到索引为 2 (3-1)的元素
        mysli1 := myarr[1:3]

        // 【第二种】
        // 1 表示从索引1开始，直到到索引为 2 (3-1)的元素     切片的第三个数，影响的只是切片的容量，而不会影响长度
        mysli2 := myarr[1:3:4]

        // 声明字符串切片
        var strList []string

        // 声明整型切片
        var numList []int

        // 声明一个空切片
        var numListEmpty = []int{}

        //  一个切片具备的三个要素：类型（Type），长度（size），容量（cap）
        a := make([]int, 2)
        b := make([]int, 2, 10)
        fmt.Println(a, b)
        fmt.Println(len(a), len(b))
        fmt.Println(cap(a), cap(b))

        数组 与 切片 有相同点，它们都是可以容纳若干类型相同的元素的容器
        数组的容器大小固定，而切片本身是引用类型，它更像是 Python 中的 list 

        // 追加一个元素
        myarr = append(myarr, 2)
        // 追加多个元素
        myarr = append(myarr, 3, 4)
        // 追加一个切片, ... 表示解包，不能省略
        myarr = append(myarr, []int{7, 8}...)
        // 在第一个位置插入元素
        myarr = append([]int{0}, myarr...)
        // 在中间插入一个切片(两个元素)
        myarr = append(myarr[:5], append([]int{5,6}, myarr[5:]...)...)
        
###  5. 数据类型，  字典与布尔类型

    // 第一种方法
    var scores map[string]int = map[string]int{"english": 80, "chinese": 85}

    // 第二种方法
    scores := map[string]int{"english": 80, "chinese": 85}

    // 第三种方法
    scores := make(map[string]int)
    scores["english"] = 80
    scores["chinese"] = 85
    
    读取元素，如果key不存在，返回其value-type的零值

    删除元素    delete(scores, "math")  元素不存在不会报错

    判断key是否存在   字典的下标读取可以返回两个值，使用第二个返回值都表示对应的 key 是否存在，若存在ok为true，若不存在，则ok为false
    math, ok := scores["math"]

    循环：
        1. 获取key 和 value
        scores := map[string]int{"english": 80, "chinese": 85}
        for subject, score := range scores {
            fmt.Printf("key: %s, value: %d\n", subject, score)
        }

    布尔类型：
        python  中 True == 1 ; False == 0
        Go      中   不同类型无法进行比较


