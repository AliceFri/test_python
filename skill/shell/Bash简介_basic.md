https://wangdoc.com/bash/condition.html

### 1. shell的含义
    外壳， 与kernel内核相对应， 用户跟内核交互的对话界面

### 2. shell的种类
    sh
    bash
    csh
    tcsh
    ksh
    zsh
    fish

echo $SHELL 查看当前设备的默认Shell

bash --version 查看bash的版本

cat /etc/shells 查看可用的shell

--------------------------------------

### 1. echo命令
    echo "hello world"  # 打印hello world
    
    -n 不换行
    -e 可以使用转义字符

    echo -n a;echo b    # 打印a，不换行，打印b

    echo -e "Hello\nWorld"    # 打印Hello\nWorld

    echo $?    # 打印上一条命令的返回值
    echo $PORT    # 打印当前环境变量PORT的值

有些命令比较长，写成多行会有利于阅读和编辑，这时可以在每一行的结尾加上反斜杠，Bash 就会将下一行跟当前行放在一起解释。
echo foo \
    bar

### 2. 分号
使得一行可以放置多个命令，上一个命令执行结束后，再执行第二个命令。

    clear; ls

### 3. && 和 ||
    Command1 && Command2    # 如果Command1成功，则执行Command2
    Command1 || Command2    # 如果Command1失败，则执行Command2


### 4. type命令
    判断一个命令的来源

    type -a ls    # 判断ls是否是一个系统命令

---------------------

## 2. 扩展

    set -f: 关闭扩展
    set +f: 打开扩展

    ~: 当前用户的home目录, 
    ~root: root用户的home目录
    echo ~+: 等同于pwd

    ？: 匹配路径里面的任意单个字符，不包括空格
        ls ?.txt   # 匹配符合条件的文件名
        ls ??.txt
        echo ?.txt
    *:  匹配路径里面的任意多个字符
        ls *txt   # 匹配符合条件的文件名

    []: [aeiou]可以匹配五个元音字母中的任意一个。
        [^abc]或[!abc]表示匹配除了a、b、c以外的字符
        echo [abc].txt
        echo [a-z].txt
    
    {}: {...}表示分别扩展成大括号里面的所有值，各个值之间使用逗号分隔
        echo Front-{A,B,C}-Back
        echo Front-{A..E}-Back

        mkdir {2007..2009}-{01..12}
        for i in {1..4}
        do
            echo $i
        done

    子命令扩展
        echo $(date)

    算术扩展
        echo $((2+3))

----------------------------

### 转义
    echo \$date     # 打印$date
    
    单引号：
        echo '$USER'    # 打印$USER

    双引号：
        $ ` \ 这三个字符在双引号里面依然有特殊含义

### Here文档
    它的格式分成开始标记（<< token）和结束标记（token）

    Here 文档内部会发生变量替换，同时支持反斜杠转义，但是不支持通配符扩展，双引号和单引号也失去语法作用，变成了普通字符。

    Here 文档的本质是重定向，它将字符串重定向输出给某个命令，相当于包含了echo命令。

    $ command << token
      string
    token

### Here 字符串
    md5sum <<< 'ddd' 
    等同于
    md5sum 'ddd'
    等同于
    echo 'ddd' | md5sum