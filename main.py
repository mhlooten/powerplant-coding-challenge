from flask import Flask
from flask_restful import Api
from REST.productionplan import Productionplan
import os

app = Flask(__name__)
api = Api(app)

api.add_resource(Productionplan, '/productionplan')

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)