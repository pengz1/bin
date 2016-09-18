#!/usr/bin/env python

import subprocess


nodes = subprocess.check_output("curl localhost:8080/api/common/nodes | python -mjson.tool | grep \"id\"",
                                shell=true)

nodes_list = nodes.split("\n")
