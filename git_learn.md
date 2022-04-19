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


#### 添加与提交
git add <filename>
git add *                       # 工作区 -> 缓存区

git commit -m "代码提交信息"      # 缓存区 -> 本地仓库HEAD 