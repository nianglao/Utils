#!/bin/sh
set -x

TABLE_NAMES=""
while getopts ":a:c:e:t:" opt; do
    case ${opt} in
        a)
            # args for cmd
            args=${OPTARG}
            echo "args: ${args}"
        ;;

        c)
            cmd=${OPTARG}
            echo "cmd: ${cmd}"
        ;;

        e)
            env=${OPTARG}
            echo "env: ${env}"
        ;;

        t)
            # comma seperated table names
            echo ${OPTARG}
            TABLE_NAMES=`echo ${OPTARG} | tr ',' ' '`
            echo "TABLE_NAMES: ${TABLE_NAMES}"
        ;;

        \?)
            echo "Invalid option: -$OPTARG"
        ;;
    esac
done