# src/app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the trained model
model = joblib.load(r'D:\SZE\PhD Dissertations\GithubAccount\iris-classification\model\iris_model.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
