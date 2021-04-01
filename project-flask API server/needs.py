from elasticsearch import Elasticsearch  # elk서버와의 통신
from flask import request, Flask
from flask_restx import Resource, Namespace, Api
from flask_cors import CORS
import datetime  # UTC로 나온 시간을 한국시간으로 맞추기 위함
es = Elasticsearch('192.168.0.241:9200')


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
