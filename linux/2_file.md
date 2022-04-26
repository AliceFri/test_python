### 文件及目录管理

#### 2.1 创建和删除

##### 创建文件夹 mkdir

##### 删除 rm
rm file
rm -rf file
rm *log     find ./ -name “*log” -exec rm {}

##### mv cp 


cp -r source_dir dest_dir

##### find

find ./ | wc -l # 查看当前目录下文件个数


------------

#### 路径
cd 
~
/

pwd: 显示当前路径

#### ls
ls -al 
ls -t
在.bashrc 中设置命令别名:
alias lsl='ls -lrt'
alias lm='ls -al|more'


------------
启动帐号后自动执行的是 文件为 .profile，然后通过这个文件可设置自己的环境变量；