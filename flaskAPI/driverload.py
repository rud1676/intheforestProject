# flask모듈을 import
from needs import es, request, Resource, Namespace, timefunc, callWazuhApi, wazuhlogin, datetime
import pandas as pd
import numpy as np
driverload = Namespace(name='driverload',
                       description="About DriverLoad 이벤트")

# 아직 회사내 컴퓨터에서 알람기능을 추가안함 곧 할예정


@driverload.route("/count")
class count(Resource):
    def post(self):
        """agent-날짜 로 count해서 chart에 뿌릴 데이터를 로드합니다"""
        agents = []
        daysago = request.json.get("date")
        # get agentlist from wazuh
        wazuhlogin()
        for r in callWazuhApi("/agents")["data"]["affected_items"]:
            agents.append(r["name"])
        print(agents)
        result = []  # query result
        chartdata = []
        for a in agents:
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
                                "match": {
                                    "agent.name": a
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
                "aggs": {
                    "date_his": {
                        "date_histogram": {
                            "field": "timestamp",
                            "interval": "day"
                        }
                    }
                }
            }

            for r in es.search(index="wazuh-alerts*", body=body)["aggregations"]["date_his"]["buckets"]:
                time = r["key_as_string"][0:10]
                count = r["doc_count"]
                result.append({"agent": a, "time": time, "count": count})

        # panda로LineChart형태로 array를 바꿔줌
        dates = pd.date_range(datetime.date.today() -
                              datetime.timedelta(days=daysago), periods=daysago+1)
        # pandas로 만들어진 df에 정보입력
        df = pd.DataFrame(np.zeros((
            daysago+1, len(agents)), int), index=dates, columns=agents)
        for r in result:
            df.at[r["time"], r["agent"]] += r["count"]

        # 반환해줄 chartdata array에 column값 넣기
        column = ["Date"]
        for a in df.columns:
            column.append(a)
        chartdata.append(column)

        # 반환해줄 chartdata에 날짜랑 해서 데이터 넣기
        for i, r in enumerate(np.array(df).tolist()):
            r.insert(0, df.index[i].strftime("%Y-%m-%d"))
            chartdata.append(r)
        return chartdata


@driverload.route('/event')
class event(Resource):
    def post(self):
        """필터링 되지 않은 driver event를 얻습니다."""
        daysago = request.json.get("date")
        body = {
            "size": 10000,
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "data.win.system.eventID": 6
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
        for s in es.search(index="wazuh-alerts*", body=body)["hits"]["hits"]:
            name = s["_source"]["agent"]["name"]
            sigstate = s["_source"]["data"]["win"]["eventdata"]["signed"]
            imageLoad = s["_source"]["data"]["win"]["eventdata"]["imageLoaded"]
            if sigstate == "true":
                signature = s["_source"]["data"]["win"]["eventdata"]["signature"]
            else:
                signature = "None"
            date_t = timefunc(s["_source"]["@timestamp"])
            result.append(
                {"agent": name, "driver": signature, "sigstate": sigstate, "imageLoad": imageLoad, "time": date_t})
        return result
