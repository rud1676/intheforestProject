from needs import es, request, Resource, Namespace, timefunc, lastPath
rdp = Namespace(
    name="service", description="RDP client 사용여부를 가져옵니다.")


@rdp.route('/get')
class userlist(Resource):
    def get(self):
        """rdp 사용과 관련된 이벤트 1024,1026"""
        body = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "data.win.system.channel": "Microsoft-Windows-TerminalServices-RDPClient/Operational"
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
            }
        }
        result = []
        for r in es.search(index="wazuh-alert*", body=body)["hits"]["hits"]:
            agent = r["_source"]["agent"]["name"]
            time = timefunc(r["_source"]["timestamp"])
            desc = r["_source"]["rule"]["description"]
            result.append({"agent": agent, "time": time, "desc": desc})

        return result
