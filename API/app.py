import os

from flask import Flask, request
import joblib
import numpy as np

app = Flask(__name__)
# a simple page that says hello
@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/predict', methods=['GET'])
def predict():
    data_user = request.args.get('input')
    data_user = data_user.split(",")
    data_user = [float(x) for x in data_user]
    pipeline = joblib.load('pipe.pkl')
    data_input = np.array([data_user])
    # data_input.reshape(-1,1)
    prediction = pipeline.predict(data_input)
    return str(prediction[0])

if __name__ == "__main__":
    app.run(debug=True)
