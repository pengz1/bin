#!/bin/bash
#!/usr/bin/expect
#Program:
#    This program is used to send IPMI commands for Intel servers
#    Below commands are supported
#    -p ipaddress: power cycle
#    -on ipaddress: power on a node
#    -off ipaddress: power off a node
#    -fru ipaddress: get fru information
#    -s ipaddress: get nodes power status
#History:
#    Created on 20150823
#For Intel WB
USERNAME=onrack
PASSWORD=onrack

#For Quanta WB
#username="admin"
#password="admin"

#For vBMC
#username="admin"
#password="admin"

date_number=`date +%Y%m%d%H%M`;

if [ $# = 1 ]; then
    if [ ! -d $1 ]; then
        exit 1
    fi
    tar_name=${1}_$date_number.tar
    tar -cvf $tar_name $1
elif [ $# = 2 ] && [ $1 = '-u' ]; then
    if [ -d $1 ]; then
        echo "You file to be uncompressed is a folder"
        exit 1
    fi
    tar -xvf $2 
else
    echo "Invalide parameters"
fi
exit 0







