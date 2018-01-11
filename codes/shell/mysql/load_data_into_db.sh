#!/bin/sh
set -x
root_dir='/data/backup/mysql'

bak_file=${1}
echo ${bak_file}

user=''
password=''
databases=''
host=''
port=3306
time mysql -u${user} -p${password} -h${host} -P${port} -e"source ${bak_file}"
