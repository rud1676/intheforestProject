from needs import es, request, Resource, Namespace, timefunc, lastPath
dnsquery = Namespace(name='dnsquery',
                     description="About dnsquery 이벤트")

# 아직 회사내 컴퓨터에서 알람기능을 추가안함 곧 할예정


@dnsquery.route("/dnsquery")
class alert(Resource):
    def get(self):
        result = []
        body = {
            "size": 1000,
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "data.win.system.eventID": 22
                            }
                        },
                        # {
                        #     "regexp": {
                        #         "data.win.eventdata.targetFilename": ".+Zone.Identifier"
                        #     }
                        # },
                        # {
                        #     "regexp": {
                        #         "data.win.eventdata.contents": ".+HostUrl.+"
                        #     }
                        # },
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
            },
            "sort": [
                {"timestamp": "desc"}
            ]
        }
        for r in es.search(index="wazuh-alert*", body=body)["hits"]["hits"]:
            time = timefunc(r["_source"]["@timestamp"])
            name = r["_source"]["agent"]["name"]
            image = lastPath(r["_source"]["data"]["win"]["eventdata"]["image"])

            query = lastPath(r["_source"]["data"]["win"]
                            ["eventdata"]["queryName"])
            result.append({"timestamp": time, "name": name,
                           "image": image, "query": query})
        return result
