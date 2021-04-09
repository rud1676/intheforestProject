from needs import Flask, Api, CORS
from driverload import driverload
from networkConnection import networkConnection
from detectProcess import detect
from fileDownList import filedown
from gamelist import gamelist
from dnsquery import dnsquery

app = Flask(__name__)
CORS(app)
api = Api(app,
          version='0.1',
          title="elk api server",
          description="로그를 쌓은 ELK에 query하는 API서버",
          terms_url="/",
          contact="rud167637@gmail.com",
          license="차후에...결정")

api.add_namespace(driverload, '/driverload')
api.add_namespace(networkConnection, '/networkConnection')
api.add_namespace(detect, '/detect')
api.add_namespace(filedown, '/filedown')
api.add_namespace(gamelist, '/gamelist')
api.add_namespace(dnsquery, '/dnsquery')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
