"""
visualization.py
Visualize student data.
"""

import matplotlib.pyplot as plt

def plot_histogram(df, column):
    plt.figure(figsize=(8,5))
    plt.hist(df[column], bins=10)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    print("Visualization module is ready.")
