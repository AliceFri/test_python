mongoexport -d vms -c vehicle__standard__value -o /cache/standard_value.dat
mongoimport -d vms -c vehicle__standard__value --drop test/users.dat

