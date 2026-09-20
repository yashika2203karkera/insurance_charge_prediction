from flask import Flask, render_template, request
from pymongo import MongoClient
import ml_model  # import our ML code

app = Flask(__name__)

# ---------------- MongoDB Setup ----------------
client = MongoClient("mongodb://localhost:27017/")  # Change if using Atlas
db = client['insurance_db']
collection = db['insurance']


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from form
    age = int(request.form['age'])
    sex = request.form['sex']
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = request.form['smoker']
    region = request.form['region']

    # Prepare input dict
    input_data = {
        'age': age,
        'sex': sex,
        'bmi': bmi,
        'children': children,
        'smoker': smoker,
        'region': region
    }

    # Predict using ML model
    predicted_charge = ml_model.predict_charge(input_data)

    return render_template('index.html', prediction=predicted_charge)

if __name__ == '__main__':
    app.run(debug=True)