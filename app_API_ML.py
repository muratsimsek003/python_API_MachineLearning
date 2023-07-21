import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import warnings
warnings.simplefilter("ignore")

app = Flask(__name__)

@app.route('/', methods=['POST'])
def predict():
     json_data = request.json
     print(json_data)
     features = [np.array(json_data)]
     prediction = model.predict(features)
     if prediction == 0:
          prediction = "Not Survived"
     elif prediction == 1:
          prediction = "Survived"
     print("Result: ", prediction)
     return jsonify("Result: ", prediction)

if __name__ == '__main__':
     model = pickle.load(open("model.pkl", "rb"))  # Load "model.pkl"
     app.run(debug=True)

# #[
#     {"Age": 85, "Sex": "1", "Embarked": "0"},
#     {"Age": 24, "Sex": '"0"', "Embarked": "1"},
#     {"Age": 3, "Sex": "1", "Embarked": "2"},
#     {"Age": 21, "Sex": "1", "Embarked": "1"}
# ]