from needs import es, request, Resource, Namespace, timefunc, lastPath
wificonnection = Namespace(
    name="wificonnection", description="네트워크 연결 호스트 이름과 함께 출력된 이벤트를 가져옵니다. channel이 NetworProfile 이벤트입니다")


@wificonnection.route('/wifi')
class userlist(Resource):
    def get(self):
        """wi-fi(사실 랜연결도 잡음)연결 감지이벤트불러오기"""
        body = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "data.win.system.channel": "Microsoft-Windows-NetworkProfile/Operational"
                            }
                        },
                        {
                            "range": {
                                "@timestamp": {
                                    "gte": "now-7d/d",
                                    "lt": "now"
                                }
                            }
                        }
                    ]
                }
            }
        }
        result = []
        for r in es.search(index="wazuh-alert*", body=body)["hits"]["hits"]:
            message = r["_source"]["data"]["win"]["system"]["message"]
            name = r["_source"]["data"]["win"]["eventdata"]["name"]
            time = timefunc(r["_source"]["timestamp"])
            agent = r["_source"]["agent"]["name"]
            connection = "판결되지 않음"
            con = False

            if message.find("식별 중...") != -1:
                continue
            if message.find("연결됨") != -1:
                con = True

            if con == True:
                connection = "연결됨"
            else:
                connection = "연결 해제"
            result.append(
                {"agent": agent, "name": name, "connect": connection, "time": time})
        # status값을 연결됨, 연결되지 않음으로 구분하기 + 이름 가져오기 + host이름 가져오기!
        return result
