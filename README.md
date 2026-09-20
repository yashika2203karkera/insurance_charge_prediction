# 🏥 Medical Insurance Charges Predictor

An end-to-end Machine Learning web application built using **Flask**, **MongoDB**, and **Python**. The application uses a trained regression model to predict personal health insurance charges based on individual health and demographic factors.

---

## 📁 Project Structure

Based on your repository tree, the files are organized as follows:

```text
pymongo1/
│
├── __pycache__/            # Compiled Python bytecode files
├── templates/
│   └── index.html          # Web frontend template for user input/results
│
├── app.py                  # Core Flask web server & routing logic
├── ml_model.py            # Machine Learning model definition/loading script
├── insert_to_mongo.py      # Script to seed/populate raw data into MongoDB
├── convert_csv_to_json.py  # Utility script to parse CSV data into JSON format
│
├── insurance.csv           # Raw medical insurance dataset
└── insurance.json          # Transformed dataset ready for MongoDB insertion
```

---

## 🛠️ Features
* **Machine Learning Backend:** Employs a pre-trained predictive model (`ml_model.py`) to forecast medical costs.
* **Database Integration:** Utilizes MongoDB via `pymongo` to store, track, or manage insurance records.
* **Responsive UI:** Provides an interactive web dashboard (`index.html`) to accept features such as age, BMI, children, and smoker status.
* **Data Pipelines:** Automated utility tools to convert tabular `.csv` files into queryable `.json` formats for direct database seeding.

---

## 🚀 Getting Started

### 1. Prerequisites & Environment Setup
Make sure you have **Python 3.13** (as indicated by your `.pyc` files) and **MongoDB** installed and running on your local machine.

Clone this repository, navigate to your root directory (`pymongo1`), and install the required dependencies:
```bash
pip install flask pymongo scikit-learn pandas numpy
```

### 2. Data Pipeline & Database Seeding (Optional)
If you want to migrate the raw `insurance.csv` data into your MongoDB collections, execute the utility scripts:

```bash
# Convert the CSV dataset into structured JSON format
python convert_csv_to_json.py

# Insert the JSON records into your MongoDB instance
python insert_to_mongo.py
```

### 3. Launching the Application
Fire up your Flask server in debug development mode:
```bash
flask run --debug
```

Once running, open your web browser and navigate to:
👉 **`http://127.0.0.1:5000`**

---

## 📊 Dataset Parameters

The underlying model predicts charges based on the standard parameters present inside your `insurance.csv`:
* **Age:** Age of primary beneficiary (Numerical)
* **Sex:** Insurance contractor gender (`female`, `male`)
* **BMI:** Body Mass Index, providing an objective view of body weight relative to height (Numerical)
* **Children:** Number of children/dependents covered by health insurance (Numerical)
* **Smoker:** Smoking status (`yes`, `no`)
* **Region:** The beneficiary's residential area in the US (`northeast`, `northwest`, `southeast`, `southwest`)
