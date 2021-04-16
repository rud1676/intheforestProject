from needs import es, request, Resource, Namespace, timefunc, datetime
from wazuhapi import userlist
networkConnection = Namespace(name='networkConnection',
                              description="About networkConnection 이벤트")


@networkConnection.route("/process")
class process(Resource):
    def post(self):
        """Network connection 정보 하루날짜-agent이름- image로 얻어옵니다."""
        daysago = request.json.get("date")
        result = []
        agents = []
        cnt = 0
        for a in userlist.get(self):
            agents.append(a["name"])
        print(daysago)
        print(agents)
        for d in range(0, int(daysago)):
            for a in agents:
                body = {
                    "size": 0,
                    "query": {
                        "bool": {
                            "must": [
                                {
                                    "match": {
                                        "data.win.system.eventID": 3
                                    }
                                },
                                {
                                    "match": {
                                        "agent.name": a
                                    }
                                },
                                {
                                    "range": {
                                        "@timestamp": {
                                            "gte": "now-"+str(d+1)+"d/d",
                                            "lt": "now-"+str(d)+"d/d",
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    "aggs": {
                        "stations": {
                            "terms": {
                                "field": "data.win.eventdata.image"
                            }
                        }
                    }
                }
                for r in es.search(index="wazuh-alert*", body=body)["aggregations"]["stations"]["buckets"]:
                    cnt += 1
                    result.append({"id": cnt, "time": str(datetime.datetime.now() -
                                                          datetime.timedelta(days=(d)))[0:10], "agent": a, "image": r["key"], "count": r["doc_count"], "date": d})
                # "query": "select DISTINCT data.win.eventdata.image,agent.name from wazuh-alert* where data.win.system.eventID='3'"
        return result


@networkConnection.route("/imageevent")
class connect(Resource):
    def post(self):
        d = request.json.get("date")
        a = request.json.get("agent")
        image = request.json.get("image")
        print(a, " ", d, " ", image)
        print("hi")
        result = []
        body = body = {
            "size": 10000,
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "data.win.system.eventID": 3
                            }
                        },
                        {
                            "match_phrase": {
                                "data.win.eventdata.image": image
                            }
                        },
                        {
                            "match": {
                                "agent.name": a
                            }
                        },
                        {
                            "range": {
                                "@timestamp": {
                                    "gte": "now-"+str(d+1)+"d/d",
                                    "lt": "now-"+str(d)+"d/d",
                                }
                            }
                        }
                    ]
                }
            }
        }
        for r in es.search(index="wazuh-alert*", body=body)["hits"]["hits"]:
            destIP = r["_source"]["data"]["win"]["eventdata"]["destinationIp"]
            destPort = r["_source"]["data"]["win"]["eventdata"]["destinationPort"]
            protocol = r["_source"]["data"]["win"]["eventdata"]["protocol"]
            ruleName = r["_source"]["data"]["win"]["eventdata"]["ruleName"]
            sourIP = r["_source"]["data"]["win"]["eventdata"]["sourceIp"]
            sourPort = r["_source"]["data"]["win"]["eventdata"]["sourcePort"]
            time = timefunc(r["_source"]["timestamp"])
            result.append({"destIP": destIP, "destPort": destPort, "protocol": protocol,
                           "ruleName": ruleName, "sourIP": sourIP, "sourPort": sourPort, "time": time})
        return result
