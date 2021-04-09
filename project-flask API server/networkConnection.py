from needs import es, request, Resource, Namespace
networkConnection = Namespace(name='networkConnection',
                              description="About networkConnection 이벤트")


@networkConnection.route("/connection")
class alert(Resource):
    def get(self):
        """SQL문으로 Network connection 정보를 얻어옵니다."""
        body = {
            "query": "select DISTINCT data.win.eventdata.image,agent.name from wazuh-alert* where data.win.system.eventID='3'"
        }

        result = []
        for r in es.index(index="_opendistro", doc_type="_sql", body=body)["datarows"]:
            image = r[0]
            name = r[1]
            result.append({"image": image, "name": name})

        return result
