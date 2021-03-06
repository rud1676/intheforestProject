from elasticsearch import Elasticsearch  # elk서버와의 통신
from flask import request, Flask
from flask_restx import Resource, Namespace, Api
from flask_cors import CORS
import datetime  # UTC로 나온 시간을 한국시간으로 맞추기 위함
import re  # regex
import pandas as pd
import numpy as np
# for wazuh api!
import json
import requests
#import urllib3
import requests
from base64 import b64encode


hostUrl = "34.64.147.254"

es = Elasticsearch(hostUrl+':9200')
#########sector for wazuh-api config!#############
protocol = 'http'
host = hostUrl
port = 55000
user = 'wazuh'
password = 'wazuh'
login_endpoint = 'security/user/authenticate'  # user authenticate path!

# url setting
login_url = f"{protocol}://{host}:{port}/{login_endpoint}"
basic_auth = f"{user}:{password}".encode()
login_headers = {'Content-Type': 'application/json',
                 'Authorization': f'Basic {b64encode(basic_auth).decode()}'}

# setting header!
requests_headers = None

# ============================########3


def timefunc(t):
    # 시간 변환 자꾸 해야되서 중복제거 => datetime struct => string으로 , 표준시간이랑 +9시간 차이나는거 조정
    times = t.replace("T", " ")[:19]
    date_t = datetime.datetime.strptime(times, '%Y-%m-%d %H:%M:%S')
    date_t = date_t + datetime.timedelta(hours=9)  # In Company not add 9
    return str(date_t)


def lastPath(l):
    l = l.split("\\")
    return l[-1]


def catchurl(l):
    """this use filedownlist.py => extract url"""
    match_g = re.compile(".+HostUrl=(.+)")
    m = match_g.match(l)
    return m.group(1)

# =====================about wazuh
# wazuh api needs token


def wazuhlogin():
    global requests_headers
    response = requests.get(login_url, headers=login_headers, verify=False)
    token = json.loads(response.content.decode())['data']['token']
    requests_headers = {'Content-Type': 'application/json',
                        'Authorization': f'Bearer {token}'}
    response = requests.get(
        f"{protocol}://{host}:{port}/?pretty=true", headers=requests_headers, verify=False)

# wazuh api call    !


def callWazuhApi(s):
    r = requests.get(f"{protocol}://{host}:{port}"+s +
                     "?pretty=true", headers=requests_headers, verify=False)
    return r.json()

# Agent 리스트 => 이름정보만 받아옴!


def getAgentData():
    agents = []
    wazuhlogin()
    for a in callWazuhApi("/agents")["data"]["affected_items"]:
        if a["name"] == "wazuh-and-beat":
            continue
        agents.append(a["name"])
    return agents
