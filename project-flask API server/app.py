from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from processCreate import ProcessCreate
from Employee import employee
from driverload import driverload
from networkConnection import networkConnection


app = Flask(__name__)
CORS(app)
api = Api(app,
          version='0.1',
          title="elk api server",
          description="로그를 쌓은 ELK에 query하는 API서버",
          terms_url="/",
          contact="rud167637@gmail.com",
          license="차후에...결정")

api.add_namespace(ProcessCreate, '/processCreate')
api.add_namespace(employee, '/employee')
api.add_namespace(driverload, '/driverload')
api.add_namespace(networkConnection, '/networkConnection')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
