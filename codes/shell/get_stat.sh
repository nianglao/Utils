#!/bin/sh
host=${1}
HOSTNAME=`ssh eng@${host} hostname`
KERNEL_VERSION=`ssh eng@${host} "uname -a | awk -F' ' '{print $3}'"`
CPU_PROCESSORS=`ssh eng@${host} "cat /proc/cpuinfo | grep processor | wc -l"`
MEMORY=`ssh eng@${host} "cat /proc/meminfo  | grep MemTotal | awk -F' ' '{print $2}'"`
MEMORY=`expr ${MEMORY} / 1048576`

REDHAT_VERSION=`ssh eng@${host} "cat /etc/redhat-release"`
DISKS=`ssh eng@${host} "df -h | grep dev/sd"`

echo "Hostname: ${HOSTNAME}"
echo "CPU Processors: ${CPU_PROCESSORS}"
echo "Memory: ${MEMORY} GB"
echo "RedHat Version: ${REDHAT_VERSION}"
echo "Kernel Version: ${KERNEL_VERSION}"
echo "Disks: ${DISKS}"
