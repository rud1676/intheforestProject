from elasticsearch import Elasticsearch  # elk서버와의 통신
from flask import request, Flask
from flask_restx import Resource, Namespace, Api
from flask_cors import CORS
import datetime  # UTC로 나온 시간을 한국시간으로 맞추기 위함
#for wazuh api!
import json
import requests
import urllib3
from base64 import b64encode
es = Elasticsearch('192.168.0.241:9200')
#########sector for wazuh-api config!#############
protocol = 'http'
host = 'localhost'
port = 55000
user = 'wazuh'
password = 'wazuh'
login_endpoint = 'security/user/authenticate' #user authenticate path!

        #url setting
login_url = f"{protocol}://{host}:{port}/{login_endpoint}"
basic_auth = f"{user}:{password}".encode()
login_headers = {'Content-Type': 'application/json',
                 'Authorization': f'Basic {b64encode(basic_auth).decode()}'}
        
        #setting header!
requests_headers =None
#########============================########3

def timefunc(t):
    # 시간 변환 자꾸 해야되서 중복제거 => datetime struct => string으로 , 표준시간이랑 +9시간 차이나는거 조정
    times = t.replace("T", " ")[:19]
    date_t = datetime.datetime.strptime(times, '%Y-%m-%d %H:%M:%S')
    date_t = date_t + datetime.timedelta(hours=9)
    return str(date_t)


def lastPath(l):
    l = l.split("\\")
    print(l)
    return l[-1]

#wazuh api needs token
def getToken():
    global requests_headers
    response = requests.get(login_url, headers=login_headers, verify=False)
    token = json.loads(response.content.decode())['data']['token']
    requests_headers = {'Content-Type': 'application/json',
                    'Authorization': f'Bearer {token}'}
    response = requests.get(f"{protocol}://{host}:{port}/?pretty=true", headers=requests_headers, verify=False)

#wazuh api call!
def callWazuhApi(s):
    print(f"{protocol}://{host}:{port}"+s+"?pretty=true")
    r = requests.get(f"{protocol}://{host}:{port}"+s+"?pretty=true", headers=requests_headers, verify=False)
    return r.json()