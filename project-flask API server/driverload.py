# flask모듈을 import
from needs import es, request, Resource, Namespace, timefunc
driverload = Namespace(name='driverload',
                       description="About DriverLoad 이벤트")

# 아직 회사내 컴퓨터에서 알람기능을 추가안함 곧 할예정


@driverload.route("/alert")
class alert(Resource):
    def get(self):
        """Alert기능이 꺼졋는지 켜졋는지 얻어옵니다."""
        body = {
            "size": 10000,
            "query": {
                "match_all": {

                }
            }
        }
        for r in es.search(index=".opendistro-alerting-config")["hits"]["hits"]:
            s = r["_source"]
            if s.get("monitor") != None:
                if s["monitor"]["name"] == "driverload event check":
                    v = s["monitor"]["enabled"]
        if v == True:
            returnValue = "green"
        else:
            returnValue = "error"
        return returnValue


@driverload.route('/event')
class event(Resource):
    def get(self):
        """필터링 되지 않은 driver event를 얻습니다."""
        body = {
            "size": 10000,
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "data.win.system.eventID": 6
                            }
                        }, {
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
        result = []
        for s in es.search(index="wazuh-alerts*", body=body)["hits"]["hits"]:
            name = s["_source"]["agent"]["name"]
            signature = s["_source"]["data"]["win"]["eventdata"]["signature"]
            date_t = timefunc(s["_source"]["@timestamp"])
            result.append(
                {"hostname": name, "driver": signature, "timestamp": date_t})
        return result
