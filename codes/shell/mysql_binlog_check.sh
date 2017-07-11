#!/bin/sh
CMD="mysqlbinlog"
PARAM="--base64-output=DECODE-ROWS --verbose"

# show master status;
# SHOW BINARY LOGS;
# SHOW BINLOG EVENTS in 'mysql-bin.000002’;
# use 'ps aux | grep mysql' to check datadir, default '/var/lib/mysql'
LOG_FILE="/var/lib/mysql/mysql-bin.000002"
DELTA_LOG="delta-log.data"

# last_lines is stored in this file
STATS_FILE="stats.conf"
if [ ! -f $STATS_FILE ];
then
    echo 0 > $STATS_FILE
fi
last_lines=`cat $STATS_FILE`
new_lines=`$CMD $PARAM $LOG_FILE | wc -l`
echo $new_lines > $STATS_FILE

tail_lines=`expr $new_lines - $last_lines`
if [ $tail_lines != 0 ];
then
    eval "$CMD $PARAM $LOG_FILE | tail -n $tail_lines > $DELTA_LOG"
    echo "Delta log stored in $DELTA_LOG"
else
    echo "Nothing changed"
fi

