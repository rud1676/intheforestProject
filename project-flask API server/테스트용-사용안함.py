# -- coding: utf-8 --
import os
import time
import re  # 정규표현식으로 문자열 추출.
# REST API를 위한 flask
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
# 크롤링 때문에 임포트
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
app = Flask(__name__)

# shadow dom 처리를 위한 함수


def expand_shadow_element(element, driver):
    shadow_root = driver.execute_script(
        'return arguments[0].shadowRoot', element)
    return shadow_root


CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hashcheck', methods=['POST'])
def hashcheck():
    print("누군가가 접속했네..? 해쉬값을 추출과정중입니다. 기다리셈")
    user = request.get_json()
    print(user["users"])  # 디버깅용 유저 입력확인
    userlist = user["users"]
    regex = re.compile("SHA256=(.+)</span>")
    regexProg = re.compile('<span ng-non-bindable="">(.+)</span>')
    # 페이지 기다리고...
    driver = webdriver.Chrome(executable_path="C:\chromedriver")
    if userlist == "":
        url = "http://34.64.102.4:5601/app/visualize#/edit/75e73080-4204-11eb-972d-b5b93cf41ed8?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15d,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:f4ab6b90-41d0-11eb-972d-b5b93cf41ed8,key:event.code,negate:!f,params:(query:'1'),type:phrase),query:(match_phrase:(event.code:'1')))),linked:!f,query:(language:kuery,query:''),uiState:(vis:(params:(sort:(columnIndex:1,direction:asc)))),vis:(aggs:!((enabled:!t,id:'1',params:(),schema:metric,type:count),(enabled:!t,id:'3',params:(field:winlog.event_data.Image.keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:30),schema:bucket,type:terms),(enabled:!t,id:'4',params:(field:winlog.event_data.OriginalFileName.keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:5),schema:bucket,type:terms),(enabled:!t,id:'2',params:(field:winlog.event_data.Hashes.keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:1),schema:bucket,type:terms)),params:(perPage:30,percentageCol:'',row:!t,showMetricsAtAllLevels:!f,showPartialRows:!f,showTotal:!f,sort:(columnIndex:!n,direction:!n),totalFunc:sum),title:'%EA%B0%9C%EC%9D%B8%20-%20%ED%95%B4%EC%89%AC%EA%B0%92%20%EB%82%98%EC%98%A8%20%ED%85%8C%EC%9D%B4%EB%B8%94(%EC%88%98%EC%A0%95%EC%A4%91)',type:table))"
    else:
        url = "http://34.64.102.4:5601/app/visualize#/edit/75e73080-4204-11eb-972d-b5b93cf41ed8?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15d,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:f4ab6b90-41d0-11eb-972d-b5b93cf41ed8,key:event.code,negate:!f,params:(query:'1'),type:phrase),query:(match_phrase:(event.code:'1'))),('$state':(store:appState),meta:(alias:!n,disabled:!f,index:f4ab6b90-41d0-11eb-972d-b5b93cf41ed8,key:host.name,negate:!f,params:(query:"+userlist+"),type:phrase),query:(match_phrase:(host.name:"+userlist + \
            ")))),linked:!f,query:(language:kuery,query:''),uiState:(vis:(params:(sort:(columnIndex:1,direction:asc)))),vis:(aggs:!((enabled:!t,id:'1',params:(),schema:metric,type:count),(enabled:!t,id:'3',params:(field:winlog.event_data.Image.keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:30),schema:bucket,type:terms),(enabled:!t,id:'4',params:(field:winlog.event_data.OriginalFileName.keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:5),schema:bucket,type:terms),(enabled:!t,id:'2',params:(field:winlog.event_data.Hashes.keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:1),schema:bucket,type:terms)),params:(perPage:30,percentageCol:'',row:!t,showMetricsAtAllLevels:!f,showPartialRows:!f,showTotal:!f,sort:(columnIndex:!n,direction:!n),totalFunc:sum),title:'%EA%B0%9C%EC%9D%B8%20-%20%ED%95%B4%EC%89%AC%EA%B0%92%20%EB%82%98%EC%98%A8%20%ED%85%8C%EC%9D%B4%EB%B8%94(%EC%88%98%EC%A0%95%EC%A4%91)',type:table))"
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_contains("개인 - 해쉬값 나온 테이블(수정중) - Elastic"))
    time.sleep(1)
    html = driver.page_source
    driver.close()
    # 30개의 해쉬값 추출 중 - in hashlist -> (num,program,hash)
    bsObj = BeautifulSoup(html, "html.parser")
    hashlist = []
    program = ""
    for i, tag in enumerate(bsObj.select("td.kbnTableCellFilter__hover span[ng-non-bindable]")):
        print(tag)
        if (i % 3 == 1):
            program = regexProg.search(str(tag)).group(1)
        elif i % 3 == 2:
            hashlist.append(
                (int((i+1) / 3), program, regex.search(str(tag)).group(1)))
    print(hashlist)

    notwhitelist = []
    with open("whitelist.txt", "r") as file_data:
        whitelists = file_data.read()
        for h in hashlist:
            if whitelists.find(h[2]) == -1:
                notwhitelist.append(h)

    return jsonify(notwhitelist)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv(
        'FLASK_RUN_PORT'), debug=True)
