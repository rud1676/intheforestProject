from needs import Flask, Api, CORS, wazuhlogin
from driverload import driverload
from networkConnection import networkConnection
from timeout import timeout
from fileDownList import filedown
from ProcessCreate import ProcessCreate
from dnsquery import dnsquery
from wificonnection import wificonnection
from service import service
from RDPClient import rdp
from wazuhapi import wazuh
from mainDash import mainDash
from AgentDash import AgentDash
from alertfunction import alert  # make after... first modify function
from login import login
app = Flask(__name__)


CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app,
          version='0.1',
          title="elk api server",
          description="로그를 쌓은 ELK에 query하는 API서버",
          terms_url="/",
          contact="rud167637@gmail.com",
          license="차후에...결정")
app.config['CORS_HEADERS'] = 'Content-Type'
api.add_namespace(driverload, '/driverload')
api.add_namespace(networkConnection, '/networkConnection')
api.add_namespace(timeout, '/timeout')
api.add_namespace(filedown, '/filedown')
api.add_namespace(ProcessCreate, '/process')
api.add_namespace(dnsquery, '/dnsquery')
api.add_namespace(wificonnection, '/wificonnection')
api.add_namespace(service, '/service')
api.add_namespace(rdp, '/rdp')
api.add_namespace(alert, '/alert')
api.add_namespace(wazuh, '/wazuh')
api.add_namespace(mainDash, '/maindash')
api.add_namespace(AgentDash, '/agentdash')
api.add_namespace(ProcessCreate, '/process')
api.add_namespace(login, '/login')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)
