from needs import es, request, Resource, Namespace, timefunc, datetime
timeout = Namespace(name='timeout',
                    description="About timeout 이벤트")


@timeout.route("/")
class alert(Resource):
    def post(self):
        """근무 시간 외에 사용하고있는가? 를 감지."""
        # get wazuh agents!
        resultApi = []
        agodays = request.json.get('data')["date"]
        for i in range(0, int(agodays)):  # 일주일 로그를 수집하기위한 i
            endday = str(datetime.datetime.now() -
                         datetime.timedelta(days=(i+1)))[0:10]
            startday = str(datetime.datetime.now() -
                           datetime.timedelta(days=(i)))[0:10]
            starttime = startday + " " + request.json.get('data')["start"]
            endtime = endday + " " + request.json.get('data')["end"]
            print(endtime, starttime)
            body = {
                "query": {
                    "bool": {
                        "must": [
                            {
                                "match_phrase": {
                                    "status": "active"
                                }
                            },
                            {
                                "range": {
                                    "timestamp": {
                                        "time_zone": "+09:00",
                                        "gte": endtime,
                                        "lte": starttime,
                                        "format": "yyyy-MM-dd HH:mm"
                                    }
                                }
                            }
                        ],
                    }
                },
                "aggs": {
                    "agent": {
                        "terms": {"field": "name"}
                    }
                }
            }
            result = es.search(index="wazuh-monitoring*",
                               body=body)["aggregations"]["agent"]["buckets"]
            if len(result) != 0:
                for r in result:
                    agent = r['key']
                    resultApi.append({"agent": agent, "date": startday})

            # 0시부터 근무 출근시간 까지 로그 수집햇음
            # 퇴근 시간 부터~ 0시까지 수집
        return resultApi
