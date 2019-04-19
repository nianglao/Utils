#!/usr/bin/expect -f
set username [lindex $argv 0 ]
set password [lindex $argv 1 ] 
set host [lindex $argv 2 ]

spawn ssh $username@$host
expect {
	"*yes/no" { send "yes\r"; exp_continue}
	"*password:" { send "$password\r"}
}
interact
