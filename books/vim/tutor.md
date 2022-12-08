### 1. vimrc
    vim ~/.vimrc    # 
    source ~/.vimrc # 使得配置生效

-------

命令行模式: 普通模式输入:号进入，Esc 切换为普通模式
可视模式： 普通模式按v键进入, 从插入模式 Ctrl-O  v进入


### 2. 起步
    vim xxx.txt        # 编辑某个文件，可同时打开多个文件
    :q, :q!, :wq       # 保存退出文件
    vim --version       # 查看版本
    ls -l | vim -       # 重定向其他命令输出内容 并进行编辑
    :qall               # 退出所有buffer


### 3. 常用命令

    set number      # 显示行号
    set nocompatible    # 不兼容vi, 
    set hidden      # 切换buffer， 不提醒保存内容
    set relativenumber number   # 设置相对行号
    set hlsearch    # 设置高亮搜索
    set ignorecase smartcase

### 4. buffers
    
    :buffers :ls :files         # 查看所有buffers
    :bnext                      # 下一个buffer
    :bprevious                  # 前一个buffer
    :buffer + 文件名/编号         # 切换到指令buffer
    Ctrl-O                      # 跳转到列表中旧的位置
    Ctrl-I                      # 跳转到列表中新的位置
    Ctrl-^                      # 跳转到先前编辑过的buffer

### 5. 搜索
    grep "ddd" 文件名              # 查看文件中是否有这个内容

---------

### 6. 普通模式 语法 v + n
    
    名词: 
        h           左
        j           下
        k           上
        l           右
        w           下一个单词的开头
        }           下一个段落
        $           当前行的行尾
    
    动词:
        y           复制
        d           删除
        c           change， 变为插入模式
        p           粘贴到光标后
        P           粘贴到光标前

    常用组合：
        y2h         向左拷贝两个字符
        d2w         删除后两个单词
        3k          光标向下移动3行
        yy          复制当前行
        dd          删除当前行
        cc          改变当前行

-----------

### 7. 在文件中移动
    
    9l      向右移动9次
    gg      跳到第一行
    G       跳到最后一行
    ...
    行导航
        0   本行第一个字符
        ^   本行第一个非空字符
        $   本行最后一个字符
    行搜索
        f   同一行向后搜索第一个匹配
        F   同一行向前搜索第一个匹配
    句子和段落跳转
        (   跳到前一个句子
        ）   跳到后一个句子
        {   跳到上一个段落
        }   跳到下一个段落
    搜索导航
        /   向后搜索一个匹配
        ？   向前搜索一个匹配
        n   重复上一次搜素，方向相同
        N   重复上一次搜索，方向相反     
        *   向后查找光标所在的完整单词
    位置标记
        ma  用a标签标记一个位置
        `a  回到a标签位置
        :marks 查看所有标签

--------------------
### 8. 输入模式
    在普通模式 输入 i 或者 o 进入 输入模式
    在输入模式 输入 Esc 进入 普通模式
    
    输入模式中：
        Ctrl-h  删除一个字符
        Ctrl-w  删除一个单词
        Ctrl-u  删除一整行
        Ctrl-o  + 普通模式命令
--------------------

### 9. 点命令
    .键可以重放上一个修改操作， 比如 dd, cwconst<esc>

### 10. 寄存器
    使用寄存器   
        "1p 粘贴1号寄存器中的内容
        :put a  输出a号寄存器中的内容到新行
    :register 查看寄存器内容
    
    命名寄存器：  "a-z        "ayiw 将yiw写入a寄存器

-------------------
### 11. 撤销
    
    最基本的撤销
    u   或者 :undo

    Ctrl-r 或者 :redo     # 恢复撤销动作

    U 会删除最近修改的行行中所有的修改， 且自身也算作一次修改

    插入模式中， Ctrl-G u 生成1个断点

------------------
### 12. 搜索与替换
    
    /   搜索
        ^   行中的第一个字符
        $   行中的最后一个字符
        候选词       /\vhello|hola
                    /hello\|hola
        搜索11开始22结束的vim      /11\zsvim\ze22

    :s/good/awesome/    将good替换为awesome

----------------------
### 13. 外部命令

    :r !{cmd}