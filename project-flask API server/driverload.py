# flask모듈을 import
from flask import request
from flask_restx import Resource, Namespace
from elasticsearch import Elasticsearch  # elk서버와의 통신
driverload = Namespace(name='driverload',
                       description="About DriverLoad 이벤트")
es = Elasticsearch('34.64.140.231:9200')


@driverload.route('/event')
class addemployee(Resource):
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
                                    "gte": "now-1d/d",
                                    "lt": "now"
                                }
                            }
                        }
                    ]
                }
            }
        }
        result = []
        for s in es.search(index="wazuh-alerts*", body=body)["hits"]["hits"]:
            name = s["_source"]["agent"]["name"]
            signature = s["_source"]["data"]["win"]["eventdata"]["signature"]
            time = s["_source"]["@timestamp"].replace("T", " ")[:19]
            result.append(
                {"hostname": name, "driver": signature, "timestamp": time})
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
