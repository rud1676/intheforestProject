from needs import es, request, Resource, Namespace
createThread = Namespace(name='createThread',
                              description="create Thread 이벤트")


@createThread.route("/thread")
class alert(Resource):
    def get(self):
        """SQL문으로 createThread 정보를 얻어옵니다."""
        body = {
            "query": "select DISTINCT data.win.eventdata.sourceImage,data.win.eventdata.targetImage,agent.name from wazuh-alert* where data.win.system.eventID='8'"
        }
        result = []
        for r in es.index(index="_opendistro", doc_type="_sql", body=body)["datarows"]:
            source = r[0]
            target = r[1]
            name = r[2]
            result.append({"source": source, "target": target, "name": name})
        return result
