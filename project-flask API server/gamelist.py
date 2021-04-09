from needs import es, request, Resource, Namespace, timefunc, lastPath
# 크롤링 때문에 임포트
gamelist = Namespace(name="gamelist", description="test")


@gamelist.route('/gamelist')
class userlist(Resource):
    def get(self):
        index = "wazuh-alerts*"
        body = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "regexp": {
                                "data.win.system.eventID": "1"

                            },
                            "regexp": {
                                "data.win.eventdata.originalFileName": "LeagueClientUx.+",
                            }
                        }
                    ]
                }
            }
        }
        result = es.search(index="wazuh-alert*", body=body)
        test = []
        gameList = {'kakao.exe': '카카오톡', 'maplestory.exe': '메이플 스토리',
                    'LeagueClientUx.exe': 'League Of Legend'}

        for r in result["hits"]["hits"]:
            data_list = r["_source"]["data"]["win"]["eventdata"]["originalFileName"]
            pc_name = r["_source"]["agent"]["name"]
            time = r["_source"]["data"]["win"]["eventdata"]["utcTime"]
            game_name = ""

            try:
                game_name = gameList[data_list]
            except:
                continue
            test.append({"Detected Games": data_list,
                         "Detected Game Name": game_name, "name": pc_name, "git statu": time})
        return {
            "images": test
        }
