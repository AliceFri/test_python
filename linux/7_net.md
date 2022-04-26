### 查询网路和端口
ss -nlpt

netstat -at # 列出所有tcp端口

netstat -l  # 列出所有监听的服务状态


netstat -antp | grep 27017
ps pid


lsof -i:27017
ps -ef | grep 30294


#### 网络路由
route -n    # 查看路由表

ping/traceroute

host domain # DNS查询
host ip     # 反向DNS查询

wget