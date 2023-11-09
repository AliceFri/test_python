mongoexport -d vms -c vehicle__standard__value -o /cache/standard_value.dat
mongoimport -d vms -c vehicle__standard__value --drop test/users.dat


mongodump --forceTableScan -h mgset-62869753/dds-rj994eaa37f5f0c41.mongodb.rds.aliyuncs.com:3717,dds-rj994eaa37f5f0c42.mongodb.rds.aliyuncs.com:3717 
-u vms_us_u -p vms_us_pwd_GBkN3GZp -d vms_us -o ./backup/2023_01_11

--authenticationDatabase=admin 

mongorestore -h localhost:27017 -d vms_us --drop vms_us/

