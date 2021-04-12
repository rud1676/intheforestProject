from needs import es, request, Resource, Namespace, timefunc, lastPath
alert = Namespace(
    name="service", description="시스템 이벤트를 불러오는 라우팅 서비스가 설치될때 이벤트 7045 등 에 의해서 그 목록들을 불러옵니다")


@alert.route('/get')
class userlist(Resource):
    def get(self):
        """7045이벤트(서비스 설치관련 이벤트임) 불러오기"""
        body = {
            "size": 10000,
            "query": {
                "match_all": {

                }
            }
        }

        result = []
        return es.search(index=".opendistro-alerting-config", body="body")
