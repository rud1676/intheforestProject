from needs import es, request, Resource, Namespace, timefunc, lastPath,catchurl
filedown = Namespace(name='filedown',
                     description="About filedown 이벤트")

# 아직 회사내 컴퓨터에서 알람기능을 추가안함 곧 할예정


@filedown.route("/filestream")
class alert(Resource):
    def post(self):
        daysago = request.json.get("date")
        result = []
        body = {
            "size": 10000,
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "data.win.system.eventID": 15
                            }
                        },
                        {
                            "regexp": {
                                "data.win.eventdata.targetFilename": ".+Zone.Identifier"
                            }
                        },
                        {
                            "regexp": {
                                "data.win.eventdata.contents": ".+HostUrl.+"
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
            },
            "sort": [
                {"timestamp": "desc"}
            ]
        }
        for r in es.search(index="wazuh-alert*", body=body)["hits"]["hits"]:
            time = timefunc(r["_source"]["@timestamp"])
            name = r["_source"]["agent"]["name"]
            prog = lastPath(r["_source"]["data"]["win"]["eventdata"]["image"])
            url = catchurl(r["_source"]["data"]["win"]["eventdata"]["contents"])
            file = lastPath(r["_source"]["data"]["win"]
                            ["eventdata"]["targetFilename"]).replace(":Zone.Identifier", "")
            result.append({"timestamp": time, "name": name,
                           "image": prog, "file": file,"url":url})
        return result
