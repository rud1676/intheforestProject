import requests
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
            record = lastPath(r["_source"]["data"]["win"]
                              ["system"]["eventRecordID"])
            result.append({"timestamp": time, "name": name,
                           "image": image, "query": query, "record": record})
        return result


@dnsquery.route("/check")
class alert(Resource):
    def get(self):
        url = 'https://www.virustotal.com/vtapi/v2/url/report'

        params = {'apikey': 'ac9eed711ba588d4ecfa6371821f13eedaa68e19d648869af18420c0463f6bcf',
                  'resource': ''}
        params['resource'] = request.args.get('domain', '')
        response = requests.get(url, params=params)
        result = []
        result.append({"date": response.json()["scan_date"],
                       "positives": response.json()["positives"],
                       "total": response.json()["total"],
                       "scans": response.json()["scans"]
                       })

        a = response.json()["scans"]
        i = 0
        for key, value in a.items():
            scans = key
            detected = value['detected']
            clean = value['result']
            result.append(
                {"scans": scans, "detected": detected, "clean": clean})
        print(result)
        return result
