#!/bin/bash
#!/usr/bin/expect
#Program:
#History:
#    Created on 20160603
opr_type="nodes"
curl_opr="POST"
operator=""
id=""
server_ip="localhost:8080"
style=" python -m json.tool"
data=""
workflow=""
while getopts 'i:d:w:' OPT;
do
    case $OPT in
        i)
            id=$OPTARG
            ;;
        d)
            data=$OPTARG
            ;;
        w)
            workflow=$OPTARG
            ;;
        ?)
            echo "Invalide parameter"
            exit 0
    esac
done
set -x 
curl -X $curl_opr -H 'Content-Type: application/json' -d @$data $server_ip/api/current/$opr_type/$id/workflows?name=Graph.$workflow | $style
set +x 

exit 0

