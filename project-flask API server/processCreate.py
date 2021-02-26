# -- coding: utf-8 --
"""
이거 미완성이다. hashcheck는 완성되지않은 부분임 크롤링하는 부분은 삭제 예정.
"""
import os
import time
import re  # 정규표현식으로 문자열 추출.
import json  # json형식 다루기
# flask모듈을 import
from flask import request, jsonify
from flask_restx import Resource, Namespace
from elasticsearch import Elasticsearch  # elk서버와의 통신
# 크롤링 때문에 임포트
ProcessCreate = Namespace(name='ProcessCreate',
                          description="About Process create - BlackList alert and so on")
es = Elasticsearch('http://34.64.140.231:9200')
print(es)
alertId = ""


@ProcessCreate.route('/BlackList')
class userlist(Resource):
    def get(self):
        """opendistro alert에 있는 블랙 리스트를 받아옵니다"""
        global alertId
        # BlackList alert 찾기
        index = ".opendistro-alerting-config"
        body = {
            "query": {
                "match_all": {}
            }
        }
        result = es.search(index=index, doc_type="_doc", body=body)
        for r in result["hits"]["hits"]:
            alert = r["_source"].get("monitor")
            if alert != None:
                alertId = r["_id"]
                if alert["name"] == "processCreate - BlackList":
                    blackalert = alert["inputs"][0]["search"]["query"]["query"]["bool"]["should"]

        # 디버깅용 - 받아온 규칙(프로세스 이미지) 실제 이미지 파일로 문자열 변환
        images = []
        for black in blackalert:
            image = black["regexp"]["data.win.eventdata.image"]["value"]
            images.append(image.replace(
                ".+", "").replace("[", "").replace("]", ""))
        print(images)
        return {
            "images": images
        }

    def put(self):
        """vue에서 받아온 image를 flitering 규칙으로 regex표현으로 바꿔서 입력합니다"""
        global alertId
        im = request.json.get('images')
        image = []
        for i in im:
            image.append(i.replace(".", "[.]"))
        print(image)
        # 메모! 스크립트로 할땐 {대신 [를 쓰더라 쉬벌]}

        # 스크립트 만드는 부분
        sc = "["
        for i in image:
            sc = sc+"['regexp':['data.win.eventdata.image':['value' : '.+"+i + \
                "','flags_value' : 65535,'max_determinized_states' : 10000,'boost' : 1.0]]],"
        sc = sc[:-1]
        sc += "]"
        body = {
            'script':  "ctx._source.monitor.inputs[0].search.query.query.bool.should = "+sc
        }
        # 엘라스틱 서치에 표현한 식을 넣어 alert로 처리합니다
        print(es.update(index=".opendistro-alerting-config",
                        id=alertId, doc_type="_doc", body=body))
        return {"test": "test"}


"""
[
    [
        'regexp':[
            'data.win.eventdata.image':[
                'value' : '.+vmplayer[.]exe',
                'flags_value' : 65535,
                'max_determinized_states' : 10000,
                'boost' : 1.0
                ]
            ]
    ],
    [
        'regexp' : [
            'data.win.eventdata.image' : [
                'value' : '.+powershell[.]exe',
                'flags_value' : 65535,
                'max_determinized_states' : 10000,
                'boost' : 1.0
                ]
            ]
    ]
]
"""
