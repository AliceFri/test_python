#### date, md5sum
echo -n $(date "+%Y_%m_%d_%H_%M_salt_vms")|md5sum|cut -d ' ' -f1

# 查看端口状态
ss -lnpt

# cp
cp -r data_mongo data_mongo_bak

# du -ah

# scp命令
scp -r root@tech:/root/mongo $(pwd)/mongo_data

# chmod
sudo chmod 777 *

# set命令
	set -ex	# -e
	
# rm命令 find命令
	find -type d -mtime +15 -name "tmp*" |xargs rm -r
	rm -r vdata-_202203*
	
# systemctl命令
cp daemon.service /lib/systemd/system/
systemctl daemon-reload
systemctl daemon.service
systemctl restart daemon.service
systemctl status daemon

# 查看服务log
journalctl -f -u daemon.service