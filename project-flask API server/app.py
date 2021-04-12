from needs import Flask, Api, CORS, getToken, callWazuhApi
from driverload import driverload
from networkConnection import networkConnection
from detectProcess import detect
from fileDownList import filedown
from gamelist import gamelist
from dnsquery import dnsquery
from wificonnection import wificonnection
from service import service
from RDPClient import rdp
from wazuhapi import wazuh
from alertfunction import alert  # make after... first modify function
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
api.add_namespace(wificonnection, '/wificonnection')
api.add_namespace(service, '/service')
api.add_namespace(rdp, '/rdp')
api.add_namespace(alert, '/alert')
api.add_namespace(wazuh, '/wazuh')
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)
