#!/bin/sh
HOSTNAME=`hostname`
KERNEL_VERSION=`uname -a | awk -F' ' '{print $3}'`
CPU_PROCESSORS=`cat /proc/cpuinfo | grep processor | wc -l`
MEMORY=`cat /proc/meminfo  | grep MemTotal | awk -F' ' '{print $2}'`
MEMORY=`expr ${MEMORY} / 1048576`

REDHAT_VERSION=`cat /etc/redhat-release`
DISKS=`df -h | grep dev/sd`

echo "Hostname: ${HOSTNAME}"
echo "CPU Processors: ${CPU_PROCESSORS}"
echo "Memory: ${MEMORY} GB"
echo "RedHat Version: ${REDHAT_VERSION}"
echo "Kernel Version: ${KERNEL_VERSION}"
echo "Disks: ${DISKS}"
