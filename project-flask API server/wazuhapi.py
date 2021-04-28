from needs import es, request, Resource, Namespace, timefunc, lastPath, callWazuhApi, wazuhlogin


wazuh = Namespace(
    name="wazuh", description="get wazuh db!")


@wazuh.route('/agents')
class userlist(Resource):
    def get(self):
        """get Agent info => ip,name,status!"""
        wazuhlogin()
        agents = []
        for r in callWazuhApi("/agents")["data"]["affected_items"]:
            # Manage PC는 제외
            if r["name"] == "wazuh-and-beat":
                continue
            agents.append(
                {"name": r["name"], "ip": r["ip"], "status": r["status"]})
        return agents
