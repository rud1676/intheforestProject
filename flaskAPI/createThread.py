from needs import es, request, Resource, Namespace
createThread = Namespace(name='createThread',
                              description="create Thread 이벤트")


@createThread.route("/thread")
class alert(Resource):
    def post(self):
        """SQL문으로 createThread 정보를 얻어옵니다."""
        body = body = {
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
        result = []
        return result
