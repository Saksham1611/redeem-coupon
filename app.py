from flask import Flask
from flask_restful import Api, Resource, reqparse
import joblib
import numpy as np


app = Flask(__name__)
api = Api(app)

#change the model type to experiment around
logres_model = joblib.load("models/logres_model.pkl")

class Predict(Resource):

    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('campaign_id')
        parser.add_argument('coupon_id')
        parser.add_argument('customer_id')

        args = parser.parse_args()  # creates dict

        X_new = np.fromiter(args.values(), dtype=str)  # convert input to array

        out = {'redemption_status': logres_model.predict([X_new])[0]}

        return out, 200
        

api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run(debug=True,port=1088)

