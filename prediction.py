"""
prediction.py
Predict academic success for new students.
"""

import joblib
import pandas as pd

def predict(file_path):
    # Load trained model
    model = joblib.load("models/student_model.pkl")

    # Load new data
    data = pd.read_excel(file_path)

    # Make predictions
    predictions = model.predict(data)

    return predictions


if __name__ == "__main__":
    print("Prediction module is ready.")
