"""
preprocessing.py
Data preprocessing functions.
"""

import pandas as pd


def clean_data(df):
    """
    Clean the dataset.
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with missing values
    df = df.dropna()

    return df


if __name__ == "__main__":
    print("Preprocessing module is ready.")
clean_data(data)
