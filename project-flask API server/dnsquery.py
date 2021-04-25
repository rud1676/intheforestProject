from needs import es, request, Resource, Namespace, timefunc, lastPath
dnsquery = Namespace(name='dnsquery',
                     description="About dnsquery 이벤트")


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
            record = lastPath(r["_source"]["data"]["win"]["system"]["eventRecordID"])
            result.append({"timestamp": time, "name": name,
                           "image": image, "query": query, "record":record})
        return result


@dnsquery.route("/check")
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
            rtype = lastPath(r["_source"]["data"]["win"]["eventdata"]["image"])

            query = lastPath(r["_source"]["data"]["win"]
                             ["eventdata"]["queryName"])
            result.append({"timestamp": time, "name": name,
                           "rtype": image, "query": query})
        return result
