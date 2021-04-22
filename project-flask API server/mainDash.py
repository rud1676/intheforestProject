from needs import es, request, Resource, Namespace, timefunc, lastPath, getAgentData
mainDash = Namespace(
    name="mainDash", description="메인 대시보드에 관한 필요한 정보를 불러오는 주소입니다.(/maindash)")


@mainDash.route('/agentactive')
class userlist(Resource):
    def post(self):
        """모든 agent에 대해 agodate만큼의 Active에 대한내용을 전부 불러옴."""
        agents = getAgentData()
        daysago = request.json.get("date")
        print(daysago)
        result = []
        for agent in agents:
            body = {
                "size": 10000,
                "query": {
                    "bool": {
                        "must": [
                            {
                                "match": {
                                    "name": agent
                                }
                            },
                            {
                                "range": {

                                    "timestamp": {
                                        "gte": "now-"+str(daysago)+"d/d",
                                        "lt": "now"
                                    }
                                }
                            }]
                    }
                },
                "sort": [
                    {"timestamp": "desc"}
                ]
            }
            data = []
            for r in es.search(index="wazuh-monitoring-*", body=body)["hits"]["hits"]:
                time = r["_source"]["timestamp"]
                status = 0
                if r["_source"]["status"] == "active":
                    status = 1
                data.append({"time": time, "status": status})
            result.append({"agent": agent, "data": data})

        return result
