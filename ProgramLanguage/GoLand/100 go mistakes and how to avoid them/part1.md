Go 使用组合的方式实现继承; 使用接口的方式来实现多态行为。
Go 中的结构体可以包含接口属性, 这样结构体能具有动态的行为。

#### 1. 变量遮蔽
    块中声明的变量可以在内部块中被重新声明。这个原理被称为变量遮蔽。
    
    总结： 尽量避免变量遮蔽, 实操中可以只允许err变量的遮蔽行为。    

### 2. 没有必要的代码嵌套

    嵌套层数过多，影响阅读

    总结： 1. 及时return 2. 遇到错误及时抛出 3. 抽出方法  实操中尽量不要有3层或以上的代码嵌套

### 3. 滥用 init 方法

    init函数没有参数也没用返回值, 不可以被调用; init函数可以在同个包内, 同个文件内被定义多次; init函数在包初始化时执行

    init函数只会执行一次, 同个文件内的init函数按照顺序执行，同个包的不同文件内的init函数，按照文件名字母序执行

    init缺点：
        1. 错误处理受限, init没有返回值, 唯一的错误处理方式就是panic, 对导入包的调用方可能不友好
        2. 不必要的依赖， 比如单元测试本不需要执行也执行了

    适用情形：
        1. 不能用声明表达式初始化的包级变量  var pc [256]byte, init中初始化
        2. 重置包级变量值, 对包级变量进行初始化
        3. 实现注册模式 sql.Register("xxx", &Driver{})
        4. 在真正开始之前验证或修复程序状态

    总结: 避免init方法滥用， 一个包中最多有一个init函数, 如果存在init函数, 请放在和包同名的文件中

### 4. 过度使用getter 和 setter
    使用Getter 和 Setter有好处：
    1. 对获取/设置进行了封装, 方便后续添加新的功能性代码
    2. 屏蔽内部实现
    3. 方便debug

    缺点就是带来了很多代码量

    总结： Getter 和 Setter的使用根据情况确认, Getter的命名不要以Get开头

### 5. 过度使用接口

    接口污染 是指用不必要的抽象来编写代码， 刻意使用接口特性，会让我们的代码难以理解

    接口越大， 抽象越弱； 接口中每增加一个方法，就会降低接口的复用性。
    什么时候使用接口：
        1. 通用的行为
        2. 解耦（策略模式等，依赖倒置）
        3. 限制行为
        

    发现抽象，而不是创造抽象。
    总结: 非必要 不使用接口。

### 6. 把接口错误的定义在生产端
    
    接口的定义权交由消费端创建具有更大的灵活性, 当然提前就知道具有很大复用性的接口可以定义在生产端，一次定义，多个客户端使用。
    且定义在生产端的接口并没有限制客户端重新定义接口。
    
    总结：接口定义在消费端，由消费端决定接口的粒度有更大的灵活性。

### 7. 返回一个接口一般是不好的做法

    返回接口，会造成对接口定义的依赖，若接口定义在另外的包中，很容易导致依赖关系混乱。

    总结： 不要返回接口，返回结构体; 函数或结构体尽量接受接口

### 8. Any Says Nothing

    type any = interface{}
    
    总结： 不要滥用any, any的表达性很弱，会导致问题在编译器发现不了； 只在确实需要接受返回任何可能的类型的场景才使用any.

### 9. 不知道何时或者怎么使用泛型
    
    func getKeys[K comparable, V any](m map[K][V]) []K {
        var keys []K
        for k := range m {
            keys = append(keys, k)
        }
        return keys
    }

    keys := getKeys[string, int](map[string][int]{"test": 1})

    引入泛型后， 接口的定义扩展为了： 类型集合
    // 要求接口实现类型的底层类型是int, 且实现了String方法    
    type customerInt interface {
        ~int
        String() string
    }
    泛型 可以用在函数参数中， 也可以用在数据结构中。

    总结： 泛型是需要时再实例化的类型，实例化时作为参数指明这些类型。 一般用在方法函数参数，数据结构中。

### 10. 类型嵌入的使用场景
    
    一个结构体的字段在声明的时候没有名字， 这个字段被称为 内嵌 embedded

    错误使用用法：
    type InMem struct {
        sync.Mutex
        m map[string]int
    }

    会将Lock和Unlock方法提升到InMem中，被暴露出去

    总结: 没有必要的理由不要使用 类型嵌入

### 11. 编写构造函数的时候, 可以考虑使用option模式

    构造函数最方便的形式是python的默认参数那种形式; go中可以用几个方法模拟:

    1. 结构体参数
    type Config struct {        // 参数最好使用指针类型, 方便辨认是未传值还是穿了零值
        Port *int
        Name *string
    }
    func NewServer(cfg Config){
    }

    2. 建造者模式, 通过builder的形式构造Config

    3. Functional options pattern 函数选项模式 (api友好, 使用一系列的自定义函数来填充配置结构体。)
    type Config struct {
        Port *int
        Name *string
    }
    
    type ConfigOption func(*Config)     // 定义一系列 修改Config的方法, 类似于建造者模式中的builder方法
    
    func WithPort(port int) ConfigOption {
        return func(cfg *Config) {
            config.Port = &port
        }
    }

    func WithName(name string) ConfigOption {
        return func(cfg *Config) {
            config.Name = &name
        }
    }

    func NewServer(opts ...ConfigOption) {
        config = &Config{}
        for  _, opt := opts {
            opt(config)
        }
        ...
    }
    
    // 使用
    NewServer()
    NewServer(WithPort(8000))
    NewServer(WithPort(8000), WithName("test"))

    总结: 构造请求里可以考虑使用函数选项模式来设置, 这样的编码模式都调用方友好！




