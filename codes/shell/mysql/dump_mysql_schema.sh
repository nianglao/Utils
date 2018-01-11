#!/bin/sh
set -x
root_dir='/data/backup/mysql'

day=`date -u '+%Y%m%d'`
echo ${day}
bak_dir=${root_dir}/${day}
echo 'backupdir is ${bak_dir}'
mkdir -p ${bak_dir}

ts=`date -u '+%Y%m%d%I%M%S'`
echo ${ts}

user=''
password=''
databases=''
host=''
port=3306

for db in ${databases};
do
    time mysqldump --no-data -u${user} -p${password} -h${host} -P${port} --databases ${db} > ${bak_dir}/$db-$ts.sql
done
