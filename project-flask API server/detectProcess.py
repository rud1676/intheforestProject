from needs import es, request, Resource, Namespace, timefunc, datetime
detect = Namespace(name='detect',
                   description="About detect 이벤트")


@detect.route("/abnormal")
class alert(Resource):
    def post(self):
        """근무 시간 외에 사용하고있는가? 를 감지."""
        print(request.json.get('data')["start"])
        result = []
        # 로그 수집 시작
        for i in range(1, 8):  # 일주일 로그를 수집하기위한 i
            n = datetime.datetime.now() - datetime.timedelta(days=i)
            startday = str(n)[0:10]
            endtime = startday + " " + request.json.get('data')["end"]
            body = {
                "size": 10000,
                "query": {
                    "bool": {
                        "must": [
                            {
                                "match_phrase": {
                                    "status": "active"
                                }
                            },                        {
                                "range": {
                                    "timestamp": {
                                        "time_zone": "+09:00",
                                        "gte": endtime,
                                        "lte": startday + " 23:59",
                                        "format": "yyyy-MM-dd HH:mm"
                                    }
                                }
                            }
                        ],
                    }
                },
                "sort": [
                    {"timestamp": "desc"}
                ]
            }
            for r in es.search(index="wazuh-monitoring*", body=body)["hits"]["hits"]:
                name = r["_source"]["name"]
                date_t = timefunc(r["_source"]["timestamp"])
                result.append({"name": name, "timestamp": date_t})

            starttime = startday + " " + request.json.get('data')["start"]
            body = {
                "size": 10000,
                "query": {
                    "bool": {
                        "must": [
                            {
                                "match_phrase": {
                                    "status": "active"
                                }
                            },                        {
                                "range": {
                                    "timestamp": {
                                        "time_zone": "+09:00",
                                        "gte": (startday + " 00:00"),
                                        "lte": starttime,
                                        "format": "yyyy-MM-dd HH:mm"
                                    }
                                }
                            }
                        ],
                    }
                },
                "sort": [
                    {"timestamp": "desc"}
                ]
            }
            for r in es.search(index="wazuh-monitoring*", body=body)["hits"]["hits"]:
                name = r["_source"]["name"]
                date_t = timefunc(r["_source"]["timestamp"])
                result.append({"name": name, "timestamp": date_t})
            # 0시부터 근무 출근시간 까지 로그 수집햇음

            # 퇴근 시간 부터~ 0시까지 수집
        return result
        """
        # 집계를 위한 쿼리
        return {"hi": "hui"}
        """
