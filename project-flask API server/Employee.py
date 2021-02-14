# flask모듈을 import
from flask import request
from flask_restx import Resource, Namespace
from elasticsearch import Elasticsearch  # elk서버와의 통신
employee = Namespace(name='employee',
                     description="ELK안에 employee를 추가하거나 정보를 받는 API")
es = Elasticsearch('34.64.102.4:9200')


@employee.route('/add')
class addemployee(Resource):
    def get(self):
        """employee와 hostname을 일치시켜 Elasticsearch에 users인덱스에 추가합니다"""
        username = request.args.get('name')
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


@employee.route('/get')
class getemployee(Resource):
    def get(self):
        """users인덱스의 employee목록을 받아옵니다"""
        users = []
        body = {
            "query": {
                "match_all": {
                }
            }
        }
        result = es.search(index="user", body=body)
        source = result['hits']["hits"]
        for s in source:
            users.append(s["_source"])
        print(users)
        return {"users": users}
