#!/usr/bin/env python

# Copyright 2016, EMC, Inc.

# -*- coding: UTF-8 -*-

"""
This script is to do Secure Erase (SE) on a compute node
Four methods/tools are integrated in this scripts
A log file will be created for each disk to be erased named after disk name, like sdx.log
"""

import subprocess
import argparse

ARG_PARSER = argparse.ArgumentParser(description='RackHD secure-erase argument')

#Basic configuration
ARG_PARSER.add_argument("-i", action="store", default='', type=str, help="identification")
ARG_PARSER.add_argument("-n", action="store", default='', type=str, help="operator name")
ARG_PARSER.add_argument("-d", action="store", default='', type=str, help="operation payload")
ARG_PARSER.add_argument("--address", action="store", default='', type=str, help="RackHD host address")
ARG_PARSER.add_argument("--jq", action="store_true", default=False, help="RackHD host address")

#Http configuration
ARG_PARSER.add_argument("-P", action="store_true", default=False, help="Http POST")
ARG_PARSER.add_argument("-D", action="store_true", default=False, help="Http DELETE")

#Node operation
ARG_PARSER.add_argument("-w", action="store_true", default='', type=str, help="workflow name")
ARG_PARSER.add_argument("-c", action="store_true", default='', type=str, help="workflow name")
ARG_PARSER.add_argument("-s", action="store_true", default='', type=str, help="workflow name")
ARG_PARSER.add_argument("-p", action="store_true", default='', type=str, help="workflow name")
ARG_PARSER.add_argument("-t", action="store_true", default='', type=str, help="workflow name")
ARG_PARSER.add_argument("-o", action="store_true", default='', type=str, help="workflow name")

#Rack operator type
ARG_PARSER.add_argument("node", action="store_true", dest="node", help="workflow operation")
ARG_PARSER.add_argument("workflow", action="store_true", dest="workflow", help="workflow operation")
ARG_PARSER.add_argument("catalog", action="store_true", dest="catalog", help="catalog operation")
ARG_PARSER.add_argument("hook", action="store_true", dest="hook", help="workflow operation")
ARG_PARSER.add_argument("poller", action="store_true", dest="poller", help="workflow operation")
ARG_PARSER.add_argument("sku", action="store_true", dest="sku", help="workflow operation")
ARG_PARSER.add_argument("tag", action="store_true", dest="tag", help="workflow operation")
ARG_PARSER.add_argument("obm", action="store_true", dest="obm", help="workflow operation")

#Direct operation
ARG_PARSER.add_argument("--dactive", action="store", default='', type=str, help="workflow operation")
ARG_PARSER.add_argument("--mock", action="store", default='', type=str, help="workflow operation")


'''
try:
    progress_output = subprocess.check_output(cmd, shell=False)
    break
except subprocess.CalledProcessError:
    progress_output = ''
'''
ARG_LIST = ARG_PARSER.parse_args()

ID = ARG_LIST.i:
NAME = ARG_LIST.n:

def get_output_stype():
    style = "python -mjson.tool"
    if ARG_LIST.jq:
        style = "jq ."

def get_rackhd_address():
    address = "http://172.31.128.1:8080"
    if ARG_LIST.address:
        address = ARG_LIST.address

def get_operator():
    operator = nodes
    if ARG_LIST.node:
        operator = "nodes";
    elif ARG_LIST.obm:
        operator = "obms";
    elif ARG_LIST.workflow:
        operator = "workflows";
    elif ARG_LIST.catalog:
        operator = "catalogs";
    elif ARG_LIST.poller:
        operator = "pollers";
    elif ARG_LIST.sku:
        operator = "skus";
    elif ARG_LIST.tag:
        operator = "tags";
    elif ARG_LIST.hook:
        operator = "hooks";
    return operator;

def get_http_method():
    http_method = "GET"
    if ARG_LIST.P:
        http_method = "POST"
    elif ARG_LIST.D:
        http_method = "DELETE"
    return http_method

def get_node_operator:
    operator = ""
    if ARG_LIST.o:
        node_operator = "obms"
    elif ARG_LIST.w:
        operator = "workflows";
    elif ARG_LIST.c:
        operator = "catalogs";
    elif ARG_LIST.p:
        operator = "pollers";
    elif ARG_LIST.s:
        operator = "skus";
    elif ARG_LIST.t:
        operator = "tags";
    return operator
