from needs import es, request, Resource, Namespace
networkConnection = Namespace(name='networkConnection',
                              description="About networkConnection 이벤트")


@networkConnection.route("/connection")
class alert(Resource):
    def get(self):
        """SQL문으로 Network connection 정보를 얻어옵니다."""
        body = {
            "query": "SELECT * FROM wazuh-alert* LIMIT 50"
        }
        print("hi")
        return es.index(index="_opendistro", doc_type="_sql", body=body)
