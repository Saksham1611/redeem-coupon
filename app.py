from flask import Flask
from flask_restful import Api, Resource, reqparse
import joblib
import numpy as np
from config import MODEL_PATH_LOGRES ,MODEL_PATH_XGBOSST 

APP = Flask(__name__)
API = Api(APP)

#change the model type to experiment around
logres_model = joblib.load(MODEL_PATH_LOGRES)

class Predict(Resource):

    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        # parser.add_argument('id')
        # parser.add_argument('petal_width')
        # parser.add_argument('sepal_length')
        # parser.add_argument('sepal_width')

        args = parser.parse_args()  # creates dict

        X_new = np.fromiter(args.values(), dtype=float)  # convert input to array

        out = {'Prediction': logres_model.predict([X_new])[0]}

        return out, 200
        

API.add_resource(Predict, '/predict')

if __name__ == '__main__':
    APP.run(debug=True, port='1080')

