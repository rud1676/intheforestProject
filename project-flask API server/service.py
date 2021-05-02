from needs import es, request, Resource, Namespace, timefunc, lastPath
service = Namespace(
    name="service", description="시스템 이벤트를 불러오는 라우팅 서비스가 설치될때 이벤트 7045 등 에 의해서 그 목록들을 불러옵니다")


@service.route('/7045')
class userlist(Resource):
    def post(self):
        """7045이벤트(서비스 설치관련 이벤트임) 불러오기"""
        daysago = request.json.get("date")
        body = {
            "size": 10000,
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "data.win.system.channel": "System"
                            }
                        },
                        {
                            "match": {
                                "data.win.system.eventID": "7045"
                            }
                        },
                        {
                            "range": {
                                "@timestamp": {
                                    "gte": "now-"+str(daysago)+"d/d",
                                    "lt": "now"
                                }
                            }
                        }
                    ]
                }
            }
        }
        print("hi")
        print(daysago)
        result = []
        for r in es.search(index="wazuh-alert*", body=body)["hits"]["hits"]:
            print(r)
            agent = r["_source"]["agent"]["name"]
            time = timefunc(r["_source"]["timestamp"])
            service = r["_source"]["data"]["win"]["eventdata"]["serviceName"]
            path = r["_source"]["data"]["win"]["eventdata"]["imagePath"]
            result.append({"agent": agent, "time": time,
                           "service": service, "path": path})

        return result
