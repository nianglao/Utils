#!/bin/sh
CPU_PROCESSORS=`cat /proc/cpuinfo | grep processor | wc -l`
MEMORY=`cat /proc/meminfo  | grep MemTotal | awk -F' ' '{print $2}'`
MEMORY=`expr ${MEMORY} / 1048576`

echo "CPU Processors: ${CPU_PROCESSORS}"
echo "Memory: ${MEMORY} GB"
