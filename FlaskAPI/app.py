import flask
from flask import Flask, jsonify, request
import json
import pickle
import numpy as np

def load_models():
    file_name = "models/model_file.pickle"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

app = Flask(__name__)
@app.route('/predict', methods=['GET'])
def predict():
    # stub input features
    request_json = request.get_json()
    x = request_json['input']
    x_in = np.array(x).reshape(1,-1)
    # load model
    model = load_models()
    prediction = model.predict(x_in)[0]
    response = json.dumps({'response': bool(prediction)})
    return response, 200

if __name__ == '__main__':
    application.run(debug=True)




# [0.49, 0.715, -5.549, 1.0, 0.0476, 0.386, 0.0, 0.311, 0.866, 130.726]