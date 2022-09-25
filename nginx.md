    docker container run -d -p 127.0.0.2:3000:80 --rm --name mynginx nginx
    -d: 后台启动
    -p： 端口映射
    --rm: 容器停止运行后，自动删除容器文件

# Nginx 简介

一个高性能的 HTTP 和 反向代理 web 服务器
优点： 占用内存小，并发能力强，安装简单，配置方便

----

## 0. 多进程模型
    
开启 master 进程， 读取并校验配置文件

开启多个子进程 worker 接受响应请求

----

## 1. 常用命令

cd /usr/local/nginx/sbin/
./nginx 启动

./nginx -s stop     停止

./nginx -s quit     安全退出

./nginx -s reload   重新加载配置文件

ps -aux | grep nginx 查看nginx进程

----

## 2. 配置

### a. 全局配置

    worker_processes 1;     # worker进程数 适合填写物理机的核心数

### b. events配置

    worker_connctions 1024;     # 每个worker进程可以创建多少连接

### c. http配置

    include mime.types;         # 引入其他配置文件， mime.types 服务器端告诉前端 返回什么类型
    default_type application/octet-stream;      # 默认返回的类型
    sendfile on;                # 数据零拷贝 
    keepalive_timeout 65;       # 保持连接最长时间

    server  # 虚拟主机
        listen 80;              # 监听端口号
        server_name localhost;  # 域名、主机名
        
        location /              # 匹配 uri
            root html;          # 目录
            index index.html index.htm; # 默认页
            
            proxy_pass http://www.baidu.com # 反向代理

        error_page  500 502 503 504  /50.html; # 转向
        location = /50.html
            root html;

----

## 3. 常用功能

虚拟主机原理： 多个域名 指向同一个ip主机, nginx负责域名解析

缺点：
    Nginx 隧道式模型（应用服务器发数据给外部时经过 nginx， 受nginx限制）

----

### 1. 反向代理

正向代理是客户端的代理     eg: vpn

反向代理是服务端的代理     eg: 访问百度，实际上访问的是不同的服务器

不支持 https 的域名反向代理

需要注意代理服务器返回 302 的情况

    http -> server -> location -> proxy_pass

----

### 2. 负载均衡

会 自动去掉down掉的机器

    http -> server -> location -> proxy_pass
    配合 http -> upstream
    upstream httpds {
        server 172.17.0.1:5000 weight=1;
        server 172.17.0.1:5001 weight=1;
    }
    # weight    权重
    # down      不参加负载均衡
    # backup    备用机
    
    1. 轮询   (无法保持会话)        1. redis 去保存 session  2. token(无状态) 代替 Cookie 和 Session
    2. 权重
    3. ip_hash, 同一ip 打到同一台机器    (动态ip 无效)
    4. least_conn   最少连接数   （没什么用， 权重控制就好）
    5. fair 根据后短服务器响应时间转发请求
    6. url_hash     定向流量转发

----

### 3. 动静分离
    
    静态文件（前端资源） 可以缓存静态资源， 提高响应速度  CDN

----

### 4. 域名解析

多域名系统： 泛域名解析    *.weibo.com -> 指向一个服务实例

短网址：    短网址域名 + 泛域名解析  dwz.cn/* ； 短url 与 真实url的字典存储在db



    http -> server -> sesver_name
    server_name 和 port 组合应该是唯一的

    # 多主机名,域名解析
    server_name a.mmban.com b.mmbam.com;

    # 通配符 域名
    server_name *.mmban.com