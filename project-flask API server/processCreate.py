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


@ProcessCreate.route('/BlackList')
class userlist(Resource):
    def get(self):
        """opendistro alert에 있는 블랙 리스트를 받아옵니다"""

        # BlackList alert 찾기
        blackalert = None
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
                if alert["name"] == "processCreate - BlackList":
                    blackalert = alert["inputs"][0]["search"]["query"]["query"]["bool"]["should"]

        # 디버깅용 - 받아온 규칙(프로세스 이미지) 실제 이미지 파일로 문자열 변환
        images = []
        for black in blackalert:
            image = black["regexp"]["data.win.eventdata.image"]["value"]
            images.append(image.replace(
                ".+", "").replace("[", "").replace("]", ""))
        print(images)
        return {"images": images}
