from needs import es, request, Resource, Namespace, timefunc, lastPath, callWazuhApi, wazuhlogin


wazuh = Namespace(
    name="wazuh", description="get wazuh db!")


@wazuh.route('/agents')
class userlist(Resource):
    def get(self):
        wazuhlogin()
        """get Agent info => ip,name,status!"""
        agents = []
        for r in callWazuhApi("/agents")["data"]["affected_items"]:
            if r["name"] == "wazuh-and-beat":
                continue
            agents.append(
                {"name": r["name"], "ip": r["ip"], "status": r["status"]})
        return agents
