### 命令

git version         # 查看版本
git help            # 查看帮助
git init            # 创建新的git仓库
git status          # 查看git仓库状态

git clone https://github.com/geeeeeeeeek/git-recipes.git    # 将Git教程clone到目录


#### 工作流
1. 工作区 working dir
2. 缓存区 index(stage)
3. HEAD  指向最新一次commit的引用

#### 配置

git config -l       # 查看所有配置信息
git config --global user.name <name>
git config --global user.email <email>

git config --global alias.st status # 添加别名

#### 查看
git status          # 显示工作目录和缓存区的状态
git log             # 提交到项目历史的信息
git log --oneline
git log -n <limit>

#### 远程仓库
git remote add origin <server>  # 连接远程服务器
git remote -v                   # 查看远程信息

#### 创建代码仓库
git init        # 创建git仓库， 创建.git目录
git init <directory>
git init --bare <directory>     # 没有工作目录的裸仓库

git clone <repo>    # clone 自动创建了一个名为 origin 的远程连接，指向原有仓库。这让和中央仓库之间的交互更加简单。
git clone <repo> <directory>

#### 添加与提交
git add <filename>
git add *                       # 工作区 -> 缓存区

git commit -m "代码提交信息"      # 缓存区 -> 本地仓库HEAD 

git push origin master          # 提交到远端仓库， 可以把master 换成你想要推送的任何分支


#### CheckOut
git checkout                    # 查看当前分支
git checkout master             # 回到master分支

git checkout <commit> <file>    # 查看文件之前的版本， 它将工作目录中的 <file> 文件变成 <commit> 中那个文件的拷贝，并将它加入缓存区。
git checkout <commit>           # 更新工作目录中的所有文件，这会使你处在分离HEAD的状态

