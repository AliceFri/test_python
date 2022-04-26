#### 1. 系统管理
uname -a
lsb_release -a

查询 cpu 信息
cat /proc/cpuinfo

$cat /proc/cpuinfo | grep processor | wc -l

查看内存信息

cat /proc/meminfo

显示当前所有的系统资源limit 信息:
ulimit – a