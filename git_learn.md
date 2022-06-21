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
git config --global pull.rebase true              # In git >= 1.7.9

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
git commit --amend --no-edit

git push origin master          # 提交到远端仓库， 可以把master 换成你想要推送的任何分支


#### CheckOut
git checkout                    # 查看当前分支
git checkout master             # 回到master分支

git checkout <commit> <file>    # 查看文件之前的版本， 它将工作目录中的 <file> 文件变成 <commit> 中那个文件的拷贝，并将它加入缓存区。
git checkout <commit>           # 更新工作目录中的所有文件，这会使你处在分离HEAD的状态

git checkout a1e8fb5 hello.py
git checkout HEAD hello.py

#### revert
git revert <commit>             # 生成1个撤销了commit引入的修改的新提交，并应用到当前分支

#### reset
git reset # 应该只用于本地修改， 

git reset <file>    # 取消缓存
git reset --hard# 重设缓冲区和工作目录，匹配最近的一次提交。除了取消缓存之外，--hard 标记告诉 Git 还要重写所有工作目录中的更改
git reset <commit> 将当前分支的末端移到 <commit>，将缓存区重设到这个提交，但不改变工作目录

git reset HEAD~2 命令将当前分支向前倒退两个提交，相当于在项目历史中移除刚创建的这两个提交。记住，这种重设只能用在 非公开 的提交中。绝不要在将提交推送到共享仓库之后执行上面的操作。

git clean  # 清除未被track的文件


#### rebase
git rebase <base>
将当前分支 rebase 到 <base>，这里可以是任何类型的提交引用（ID、分支名、标签，或是 HEAD 的相对引用）。

#### 提交到远程
git checkout master
git fetch origin master
git rebase -i origin/master # git pull = git fetch + git merge/git rebase
# Squash commits, fix up commit messages etc.
git push origin master

git push <remote> <branch>  # 将指定的分支推送到remote上。 它会在目标仓库中创建一个本地分支

git push --force <remote> <branch> # 强制推送，即使目标分支已经存在


#### 使用分支
git branch          # 列出仓库中所有分支
git branch <branch> # 创建一个分支，不会切换
git branch -d <branch> # 删除分支

git branch -m <branch> # 命名

git switch          # 切换分支

git checkout <existing-branch>
git checkout -b <new-branch>
git checkout -b <new-branch> <existing-branch>


git merge <branch>  # 将指定分支并入当前分支


#### 例子快速向前
-开始新功能
git checkout -b new-feature master
-编辑文件
git add <file>
git commit -m "开始新功能"
-编辑文件
git add <file>
git commit -m "完成功能"
-合并new-feature分支
git checkout master
git merge new-feature
git branch -d new-feature


#### 测试提交
git pull origin dev

[//]: # (git fetch )

git branch --set-upstream-to=origin/dev qx_dev
git push origin qx_dev




#### 撤销commit中单个文件的修改
git log <filename>
git reset <>