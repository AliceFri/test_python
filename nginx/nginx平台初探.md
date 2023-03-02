### Question
Q: nginx 怎么控制多个worker 不会出现1个很忙，其他很闲的情况
A: worker 竞争连接时， 当某个worker可用连接数少于 1 / 8 时， 则会让出竞争机会给其他worker

### nginx 架构

#### 1. 进程模型
    一个 master 进程， 多个 worker 进程，master 进程主要用来管理 worker 进程（向 worker 发送信号， 监控 worker 状态）。
    每个 worker 单线程。
    worker 进程是对等的， worker 同等竞争来自客户端的请求， 相互独立。
    worker 通过争抢 互斥锁 抢占客户端请求。
    ./nginx -s reload 重启nginx, 是启动一个新的nginx进程 ->  master进程 -> worker进程

    

#### 2. 事件模型
    异步非阻塞
    
    事件模型： 阻塞（会让出cpu, 上下文切换） -> 非阻塞轮询（轮询浪费） -> 非阻塞 epoll  (同时监控多个事件，调用epoll是阻塞的，但可以设置超时时间)

    epoll 模型：
        没有多线程的上下文切换
        并发数只占用内存，轻量级

#### 3. 定时器模型
    红黑树

----------------

### nginx 基础概念

#### 1. connection
    tcp 连接的封装
    
    nginx启动时， master进程会创建好 对监听端口，ip的 socket。 
    nginx也可作为连接的客户端， 创建ngx_connection_t 结构体， 发起请求， 封装socket 

    nginx每个进程的同时连接数的上限， ulimit -n 

    每个worker进程都有一个独立的连接池， 连接池的大小就是最大连接数 worker_connections
    先创建好ngx_connection_t结构的数组， 通过free_connections 来保存所有的空闲ngx_connection_t

#### 2. request
    http 请求的封装

##### 2.1 keepalive
    长连接: 一个tcp连接上面执行多个请求，（必须要确定请求头和响应体的长度）
    会等待下一次请求， 只会等待keepalive_timeout时间

##### 2.2 pipe
    基于长连接， 不需要等第一个请求完成后，再进行第二个请求
    nginx仍然是一个请求一个请求的处理，只是把请求放到了buffer里。

##### 2.3 lingering_close
    延迟关闭， nginx关闭连接时， 先关闭tcp连接的写，等待一段时间后再关掉连接的读。
    延迟关闭，是为了避免客户端未收到消息，就断开连接了，给个反应时间。

---------

### nginx 基本数据结构

#### 1. ngx_str_t
    带长度的字符串结构 ngx_str_t
    好处：
        O(1) 获取字符串长度
        可以 两个变量引用同一块内存 （必须很谨慎的去修改一个字符串）

#### 2. ngx_pool_t
    提供了一种机制，帮助管理一系列的资源， 对这些资源的分配，使用，释放统一进行。
    
    可能会造成某些资源不会提前释放， 但是减轻了程序员分别管理每个资源的的生命周期问题。

#### 3. ngx_array_t
    连续内存， 带容量 nalloc 和 size ， 增长到nalloc时，触发扩容

#### 4. ngx_hash_t
    开链法 解决哈希冲突      只能一次初始化，不能添加删除元素

#### 5. ngx_hash_wildcard_t
    处理带有通配符的域名的匹配问题 （只支持通配符在前或者通配符在后） www.abc.*
    {www: {abc: 1}}

#### 6. ngx_hash_combined_t
    组合类型
    ngx_hash_t hash;
    ngx_hash_wildcard_t *wc_head;
    ngx_hash_wildcard_t *wc_tail;

#### 7. ngx_hash_keys_arrays_t
    

#### 8. ngx_chain_t
    链表结构    
    ngx_buf_t   实际数据
    ngx_chain_t next 指针指向下一个节点

#### 9. ngx_list_t
    它的节点不像我们常见的list的节点，只能存放一个元素，ngx_list_t的节点实际上是一个固定大小的数组
    类似于下面的结构[[1, 1, 1], [12, 12, 21], [9, null, null]]

#### 10. ngx_queue_t
    双向链表

---------

### nginx 配置系统

#### 简单配置项  
    
    error_page   500 502 503 504  /50x.html;

#### 复杂配置项
    
    location / {
        root   /home/jizhao/nginx-book/build/html;
        index  index.html index.htm;
    }

#### 指令上下文

    作用域
    main: nginx运行时与具体业务功能无关的一些参数（工作进程数， 运行的身份等）
    http: 提供http服务相关的一些参数 keepalive, gzip等
    server: http服务上支持若干虚拟主机， 每个虚拟主机对应一个server配置项
    location: http服务，对应特定的URL的一系列配置项
    mail: 实现email相关的代理时，共享的一些配置项

----------

### nginx的模块化体系结构

nginx将各功能模块组织成一条链，当有请求到达的时候，请求依次经过这条链上的部分或者全部模块，进行处理。每个模块实现特定的功能。例如，实现对请求解压缩的模块，实现SSI的模块，实现与上游服务器进行通讯的模块，实现与FastCGI服务进行通讯的模块。

有两个模块比较特殊，他们居于nginx core和各功能模块的中间。这两个模块就是http模块和mail模块。这2个模块在nginx core之上实现了另外一层抽象，处理与HTTP协议和email相关协议（SMTP/POP3/IMAP）有关的事件，并且确保这些事件能被以正确的顺序调用其他的一些功能模块。

#### 模块的分类

event module: 事件处理机制
phase handler: 负责处理客户端请求并产生待响应内容
output filter: 对输出的内容进行处理， 例如，可以实现对输出的所有html页面增加预定义的footbar一类的工作，或者对输出的图片的URL进行替换之类的工作。
upstream:   反向代理， 特殊的handler, 只不过响应内容不是由自身产生，而是由后端响应
load-balancer: 负载均衡