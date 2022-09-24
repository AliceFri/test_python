    docker container run -d -p 127.0.0.2:3000:80 --rm --name mynginx nginx
    -d: 后台启动
    -p： 端口映射
    --rm: 容器停止运行后，自动删除容器文件

# Nginx 简介

一个高性能的 HTTP 和 反向代理 web 服务器
优点： 占用内存小，并发能力强，安装简单，配置方便

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

    //全局配置
        
    events{
        worker_connections 1024;    // 连接数
    }

    http{
        // http配置

        upstream upstream1 {
            // 负载均衡配置
            server 127.0.0.1:8080 weight=1;
            server 127.0.0.1:8081 weight=1;
        }

        server {
            listen 80;
            server_name localhost;
            // 代理
            location / {
                root html;
                index index.html index.htm;
                proxy_pass http://upstream1;
            }
            location /another {
                // 代理
            }
        }

        server {
            listen 443;
            server_name localhost;
            // 代理
        }
    }
        



----

## 3. 常用功能

----

### 1. 反向代理

正向代理是客户端的代理     eg: vpn

反向代理是服务端的代理     eg: 访问百度，实际上访问的是不同的服务器

----

### 2. 负载均衡

    推荐用 redis 去保存 session
    
    1. 轮询
    2. 权重
    3. hash, 同一ip 打到同一台机器

----

### 3. 动静分离
    
    静态文件（前端资源） 可以缓存静态资源， 提高响应速度  CDN
    