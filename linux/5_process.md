#### 进程管理

##### 1. 查询进程

ps -ef  # 查询正在进行的进程信息

ps -ef | grep colin115

pgrep -l docker # 查询与docker相关的进程


##### 2. lsof

lsof -i:27017   # 查看27017端口的进程打开的文件

lsof -u

##### 3. 终止进程
kill pid
监控
kill -9 3434


##### 4. 分析线程栈 pmap
pmap pid

pstree