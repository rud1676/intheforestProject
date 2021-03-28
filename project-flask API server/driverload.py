# flask모듈을 import
from flask import request
from flask_restx import Resource, Namespace
import datetime  # UTC로 나온 시간을 한국시간으로 맞추기 위함
import time
from elasticsearch import Elasticsearch  # elk서버와의 통신
driverload = Namespace(name='driverload',
                       description="About DriverLoad 이벤트")
es = Elasticsearch('34.64.140.231:9200')


@driverload.route("/alert")
class alert(Resource):
    def get(self):
        """Alert기능이 꺼졋는지 켜졋는지 얻어옵니다."""
        body = {
            "size": 10000,
            "query": {
                "match_all": {

                }
            }
        }
        for r in es.search(index=".opendistro-alerting-config")["hits"]["hits"]:
            s = r["_source"]
            if s.get("monitor") != None:
                if s["monitor"]["name"] == "driverload event check":
                    v = s["monitor"]["enabled"]
        if v == True:
            returnValue = "green"
        else:
            returnValue = "error"
        return returnValue


@driverload.route('/event')
class event(Resource):
    def get(self):
        """필터링 되지 않은 driver event를 얻습니다."""
        body = {
            "size": 10000,
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "data.win.system.eventID": 6
                            }
                        }, {
                            "range": {
                                "@timestamp": {
                                    "gte": "now-7d/d",
                                    "lt": "now"
                                }
                            }
                        }
                    ]
                }
            },
            "sort": [
                {"timestamp": "desc"}
            ]
        }
        result = []
        for s in es.search(index="wazuh-alerts*", body=body)["hits"]["hits"]:
            name = s["_source"]["agent"]["name"]
            signature = s["_source"]["data"]["win"]["eventdata"]["signature"]
            times = s["_source"]["@timestamp"].replace("T", " ")[:19]
            date_t = datetime.datetime.strptime(times, '%Y-%m-%d %H:%M:%S')
            date_t = date_t + datetime.timedelta(hours=9)
            # 2021-03-25 23:50:56
            result.append(
                {"hostname": name, "driver": signature, "timestamp": str(date_t)})
        return result

    def post(self):
        """driver event를 얻습니다."""
        arg = request.args.get('arg')
        hostname = request.args.get('host')
        doc = {
            "host": hostname,
            "name": username,
        }
        body = {
            "query": {
                "match": {
                    "host": hostname
                }
            }
        }
        result = es.search(index="user", body=body)
        if result['hits']['total']['value'] == 0:
            es.index(index="user", doc_type="_doc", body=doc)
            result = "success"
        else:
            result = "fail"
        return {"state": result}
