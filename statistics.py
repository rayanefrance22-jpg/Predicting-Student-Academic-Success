"""
statistics.py
Statistical analysis of the dataset.
"""

import pandas as pd

def describe_data(df):
    print("\nDataset Summary")
    print(df.describe())

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

if __name__ == "__main__":
    print("Statistics module is ready.")
