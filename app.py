import numpy as np
import pandas as pd 
import joblib
from flask import Flask, request, render_template , url_for

app = Flask(__name__)

# Load the trained model (adjust the path as needed)

try:
    model = joblib.load('./Anemia-Sense/model/model.joblib')
except FileNotFoundError:
    print("Model file not found. Please check the file path.")
    model = None

# Routing to home.html

@app.route('/')
def home():
    return render_template('home.html')

# Routing to about.html

@app.route('/about')
def about():
    return render_template('about.html')

# Routing to contact.html

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Routing to predict.html

@app.route('/predict', methods=['POST', 'GET'])
def predict():

    # If the form is submitted

    if request.method == 'POST':
        try:

            # Getting the values from the form
            
            Hemoglobin = float(request.form.get('hemoglobin'))
            MCH = float(request.form.get('mch'))
            MCHC = float(request.form.get('mchc'))
            MCV = float(request.form.get('mcv'))
            Gender = request.form.get("gender")
            if Gender.strip().lower() == 'male':
                Gender = 0
            else:
                Gender = 1

            # Converting the values to a numpy array to feed to the model

            features_values = np.array([[Gender, Hemoglobin, MCH, MCHC, MCV]])


            if model is None:
                return "Model not loaded. Please check the model file."
            
            # Predicting the result

            prediction = model.predict(features_values)
            result = prediction[0]

            if result == 0:
                result_text = "You don't have any Anemic Disease"
            elif result == 1:
                result_text = "You have Anemic Disease"

            text = "Hence, based on calculation: "

            return render_template("result.html", prediction_text=text + str(result_text))
        except Exception:
            print("Error occurred")
            return render_template('predict.html', error_message="An error occurred during prediction.")
        
    # If the predict.html is to be loaded

    else:
        return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)