from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
import pickle

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client['insurance_db']
collection = db['insurance']

# Fetch data from MongoDB
data = pd.DataFrame(list(collection.find()))

# One-hot encode categorical variables
cat_cols = ['sex', 'smoker', 'region']
encoder = OneHotEncoder(sparse_output=False, drop='first')
encoded = pd.DataFrame(encoder.fit_transform(data[cat_cols]), columns=encoder.get_feature_names_out(cat_cols))

X = pd.concat([data[['age', 'bmi', 'children']], encoded], axis=1)
y = data['charges']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)


def predict_charge(input_dict):
    df = pd.DataFrame([input_dict])
    encoded_input = pd.DataFrame(encoder.transform(df[cat_cols]), columns=encoder.get_feature_names_out(cat_cols))
    X_input = pd.concat([df[['age', 'bmi', 'children']], encoded_input], axis=1)
    prediction = model.predict(X_input)[0]
    return round(prediction, 2)