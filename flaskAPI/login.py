from needs import es, request, Resource, Namespace, timefunc, lastPath
login = Namespace(
    name="service", description="시스템 이벤트를 불러오는 라우팅 서비스가 설치될때 이벤트 7045 등 에 의해서 그 목록들을 불러옵니다")


@login.route('/put')
class userlist(Resource):
    def post(self):
        user = {
            "name": request.json.get("name"),
            "password": request.json.get("password"),
            "id": request.json.get("id"),
            "companyid": request.json.get("companyid"),
            "valid": request.json.get("valid"),
            "admin": request.json.get("admin"),
            "phone": request.json.get("phone"),
            "addr": request.json.get("addr")
        }
        doc = {
            "size": 10000,
            "query": {
                "match": {
                    "id": user["id"]
                }
            },
        }
        if es.search(index="userdb", body=doc)["hits"]["total"]["value"] > 0:
            return {"message": "이미 존재하는 아이디입니다."}
        else:
            print(es.index(index="userdb", doc_type="_doc", body=user))
        return {"message": "아이디 등록 완료"}


@login.route('/logon')
class userlist(Resource):
    def post(self):
        user = {
            "id": request.json.get("id"),
            "password": request.json.get("password"),
        }
        doc = {
            "size": 10000,
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "id": user["id"]
                            }
                        },
                        {
                            "match": {
                                "password": user["password"]
                            }
                        }
                    ]
                }
            },
        }
        result = es.search(index="userdb", body=doc)["hits"]
        if result["total"]["value"] > 0:
            print(result)
            if result["hits"][0]["_source"]["valid"] == False:
                return {"state": "관리자 승인을 기다리세요!"}
        else:
            return {"state": "아이디와 비밀번호를 확인해주세요"}
        return {"state": "success", "user": result["hits"][0]["_source"]}


@login.route('/getusers')
class userlist(Resource):
    def get(self):
        doc = {
            "size": 10000,
            "query": {
                "match_all": {}
            },
        }
        users = []
        for r in es.search(index="userdb", body=doc)["hits"]["hits"]:
            users.append(r["_source"])
        return users
