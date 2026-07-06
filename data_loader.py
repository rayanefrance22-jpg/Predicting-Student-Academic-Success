"""
data_loader.py
Loads the student dataset.
"""

def load_data():
    print("Loading student dataset...")

if __name__ == "__main__":
    load_data()



import pandas as pd

def load_data():
    return pd.read_csv("student_data.csv")
