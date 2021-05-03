from needs import es, request, Resource, Namespace, timefunc, lastPath
# 크롤링 때문에 임포트
ProcessCreate = Namespace(name="ProcessCreate", description="test")


@ProcessCreate.route('/getEvent')
class userlist(Resource):
    def post(self):
        """ProcessCreate이벤트 정보를 다 받아옵니다!"""
        daysago = request.json.get("date")
        result = []
        body = {
            "size": 10000,
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "data.win.system.eventID": 1
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
        for r in es.search(index="wazuh-alert*", body=body)["hits"]["hits"]:
            dic = {}
            eventdata = r["_source"]["data"]["win"]["eventdata"]
            dic["time"] = timefunc(r["_source"]["timestamp"])
            dic["agent"] = r["_source"]["agent"]["name"]

            if "originalFileName" in eventdata:
                dic["originalFileName"] = eventdata["originalFileName"]
            else:
                dic["originalFileName"] = "..."

            if "image" in eventdata:
                dic["image"] = eventdata["image"]
            else:
                dic["image"] = "..."

            if "hashes" in eventdata:
                dic["hashes"] = eventdata["hashes"]
            else:
                dic["hashes"] = "..."

            if "company" in eventdata:
                dic["company"] = eventdata["company"]
            else:
                dic["company"] = "..."

            if "description" in eventdata:
                dic["description"] = eventdata["description"]
            else:
                dic["description"] = "..."

            if "fileVersion" in eventdata:
                dic["fileVersion"] = eventdata["fileVersion"]
            else:
                dic["fileVersion"] = "..."

            if "integrityLevel" in eventdata:
                dic["integrityLevel"] = eventdata["integrityLevel"]
            else:
                dic["integrityLevel"] = "..."

            if "parentCommandLine" in eventdata:
                dic["parentCommandLine"] = eventdata["parentCommandLine"]
            else:
                dic["parentCommandLine"] = "..."

            if "parentImage" in eventdata:
                dic["parentImage"] = eventdata["parentImage"]
            else:
                dic["parentImage"] = "..."

            if "product" in eventdata:
                dic["product"] = eventdata["product"]
            else:
                dic["product"] = "..."

            if "processId" in eventdata:
                dic["processId"] = eventdata["processId"]
            else:
                dic["processId"] = "..."

            if "parentProcessId" in eventdata:
                dic["parentProcessId"] = eventdata["parentProcessId"]
            else:
                dic["parentProcessId"] = "..."
            result.append(dic)

        return result
