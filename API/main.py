import pandas as pd
from flask import Flask, request, jsonify
import pickle
import numpy as np


app = Flask(__name__)

# ['LUAS BANGUNAN (m2)', 'LUAS TANAH (m2)', 'KAMAR TIDUR', 'KAMAR MANDI',
#        'NOMOR TELEPON']


# Load the .pkl model file
with open('old/model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.json

    print(data)

    # Create a DataFrame from the request data
    df = pd.DataFrame(data, index=[0])

    print(df.to_string())

    # Rename the columns
    df = df.rename(columns={
        'luas_bangunan':'LUAS BANGUNAN (m2)',
         'luas_tanah':'LUAS TANAH (m2)',
        'kamar_tidur': 'KAMAR TIDUR',
         'kamar_mandi':'KAMAR MANDI',
         'nomor_telepon':'NOMOR TELEPON'
    })
    print(df.to_string())
    # Pass the DataFrame to the model for prediction
    result = model.predict(df)

    print(result)

    # Create a response dictionary
    response = {'prediction': result[0]}  # Assuming model returns a single prediction

    # Return the response as JSON
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)