from flask import Flask
from flask_restful import Api
from REST.productionplan import Productionplan

app = Flask(__name__)
api = Api(app)

api.add_resource(Productionplan, '/productionplan')

if __name__ == "__main__":
  app.run(port=8888)