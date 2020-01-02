import ModelService

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Controller:
    class Model(Resource):
        def get(self):
            return ModelService.ModelService.getModel(1).content


api.add_resource(Controller.Model, '/')

if __name__ == "__main__":
    app.run(port='5002')