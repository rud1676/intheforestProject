from needs import es, request, Resource, Namespace, timefunc, lastPath
rdp = Namespace(
    name="service", description="RDP client 사용여부를 가져옵니다.")


@rdp.route('/get')
class rdpEventGet(Resource):
    def post(self):
        daysago = request.json.get("date")
        """rdp 사용과 관련된 이벤트 1024,1026"""
        body = {
            "size": 10000,
            "query": {
                "bool": {
                    "must": [
                        {
                            "range": {
                                "@timestamp": {
                                    "gte": "now-"+str(daysago)+"d/d",
                                    "lt": "now"
                                }
                            }
                        }
                    ],
                    "should": [
                        {
                            "match": {
                                "data.win.system.channel": "Microsoft-Windows-TerminalServices-RDPClient/Operational"
                            }
                        },
                        {
                            "match": {
                                "data.win.system.providerName": "chromoting",
                            }
                        },
                    ],
                    "minimum_should_match": 1,
                    "boost": 1,
                }
            }
        }
        result = []
        for r in es.search(index="wazuh-alert*", body=body)["hits"]["hits"]:
            agent = r["_source"]["agent"]["name"]
            time = timefunc(r["_source"]["timestamp"])
            desc = r["_source"]["rule"]["description"]
            result.append({"agent": agent, "time": time, "desc": desc})

        return result
