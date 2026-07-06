"""
model.py
Train a machine learning model to predict student academic success.
"""

import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model(X, y):
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create the model
    model = RandomForestClassifier(random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(model, "models/student_model.pkl")

    return model, X_test, y_test


if __name__ == "__main__":
    print("Model module is ready.")
