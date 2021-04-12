from needs import es, request, Resource, Namespace, timefunc, lastPath, callWazuhApi


wazuh = Namespace(
    name="wazuh", description="get wazuh db!")


@wazuh.route('/agents')
class userlist(Resource):
    def get(self):
        """get Agent info => ip,name,status!"""
        agents = []
        for r in callWazuhApi("/agents")["data"]["affected_items"]:
            agents.append({"name":r["name"],"ip":r["ip"],"status":r["status"]})
        return agents
