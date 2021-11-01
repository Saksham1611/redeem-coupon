import pickle
from flask import Flask
from flask_restful import Api, Resource, reqparse
import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

#change the model type to experiment around
logres_model = joblib.load("models/logres_model.pkl")

# Create flask app
flask_app = Flask(__name__)
model = joblib.load(open("models/logres_model.pkl", "rb"))
with open("models/one_hot.pkl","rb") as f:
    ohe=pickle.load(f)

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    # https://stackoverflow.com/questions/51420032/using-saved-sklearn-model-to-make-prediction
    float_features = [int(x) for x in request.form.values()]
    features = np.array(float_features).reshape(1,-1)
    features=features.astype(str)
    features=ohe.transform(features)
    print(f"Shape of features {features.shape}")
    prediction = model.predict(features)

    return render_template("index.html", prediction_text = "Redemption_Status {}".format(prediction))

if __name__ == "__main__":
    flask_app.run(debug=True)

