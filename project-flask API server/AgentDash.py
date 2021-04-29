from needs import es, request, Resource, Namespace, timefunc, lastPath, getAgentData, wazuhlogin, callWazuhApi, pd, np
AgentDash = Namespace(
    name="AgentDash", description="AGENT 대시보드에 관한 필요한 정보를 불러오는 주소입니다.(/agentdash)")


@AgentDash.route('/scanPortData')
class scanPortData(Resource):
    def post(self):
        """Agent의 이름을 받아서 사용중인 PortData를 가져옵니다!"""
        wazuhlogin()
        agentName = request.json.get("agent")
        result = []
        agentid = ""
        for r in callWazuhApi("/agents")["data"]["affected_items"]:
            if r["name"] == agentName:
                agentid = r["id"]
                break
        apiResult = callWazuhApi(
            "/syscollector/"+agentid+"/ports")["data"]["affected_items"]
        for r in apiResult:
            if "state" in r:
                result.append({"InnerIP": r["local"]["ip"], "InnerPort": r["local"]["port"], "OutIP": r["remote"]["ip"], "OutPort": r["remote"]["port"], "status": r["state"],
                               "protocol": r["protocol"], "process": r["process"]})
        return result


@AgentDash.route('/scanProcesses')
class scanProcesses(Resource):
    def post(self):
        """Agent의 이름을 받아서 사용중인 ProcessData를 가져옵니다!"""
        wazuhlogin()
        agentName = request.json.get("agent")
        result = []
        agentid = ""
        for r in callWazuhApi("/agents")["data"]["affected_items"]:
            if r["name"] == agentName:
                agentid = r["id"]
                break
        apiResult = callWazuhApi(
            "/syscollector/"+agentid+"/processes")["data"]["affected_items"]
        t = apiResult[0]["scan"]["time"].replace("Z", "").replace("T", " ")
        for r in apiResult:
            if "cmd" in r:
                result.append({"process": r["name"], "PID": r["pid"], "PPID": r["ppid"],
                               "session": r["session"], "InThreads": r["nlwp"], "priority": r["priority"], "Command": r["cmd"]})
            else:
                result.append({"process": r["name"], "PID": r["pid"], "PPID": r["ppid"],
                               "session": r["session"], "InThreads": r["nlwp"], "priority": r["priority"], "Command": "..."})
        data = {"result": result, "time": t}
        return data
# {protocol}://{host}:{port}/syscollector/{agent_id}/processes


@AgentDash.route("/ScanPackage")
class ScanPackage(Resource):
    def post(self):
        wazuhlogin()
        agentName = request.json.get("agent")
        result = []
        agentid = ""
        for r in callWazuhApi("/agents")["data"]["affected_items"]:
            if r["name"] == agentName:
                agentid = r["id"]
                break
        apiResult = callWazuhApi(
            "/syscollector/"+agentid+"/packages")["data"]["affected_items"]

        for r in apiResult:
            dic = {}
            dic["Program"] = r["name"]
            if "vendor" in r:
                dic["Company"] = r["vendor"]
            else:
                dic["Company"] = "..."
            if "location" in r:
                dic["Path"] = r["location"]
            else:
                dic["Path"] = "Unknown"
            if "install_time" in r:
                dic["Install_time"] = r["install_time"]
            else:
                dic["Install_time"] = "Unknown"
            result.append(dic)
        return result
