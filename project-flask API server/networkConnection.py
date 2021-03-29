from needs import es, request, Resource, Namespace
networkConnection = Namespace(name='networkConnection',
                              description="About networkConnection 이벤트")


@networkConnection.route("/alert")
class alert(Resource):
    def get(self):
        """Alert기능이 꺼졋는지 켜졋는지 얻어옵니다."""
        body = {
            "size": 10000,
            "aggs": {
                "stations": {
                    "terms": {
                        "field": "data.win.eventdata.image"
                    }
                }
            }
        }  # 집계를 위한 쿼리
        for r in es.search(index=".opendistro-alerting-config")["hits"]["hits"]:
            s = r["_source"]
            if s.get("monitor") != None:
                if s["monitor"]["name"] == "networkConnection event check":
                    v = s["monitor"]["enabled"]
        if v == True:
            returnValue = "green"
        else:
            returnValue = "error"
        return returnValue
