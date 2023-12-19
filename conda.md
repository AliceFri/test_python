conda create --name myenv python=3.11
conda activate ENV_NAME


conda info --envs
conda install PACKAGES

conda list  查看安装的包
conda search 查询包
conda install pkg==version 安装包
conda update pkg        更新包
conda remove pkg        移除包

conda中有的， 推荐用conda安装， conda没有的，再用pip安装


conda env export > envname.yml  导出包文件

conda install pip
pip install -r requirements.txt