from src.data_loader import load_data
from src.preprocessing import clean_data

data = load_data()

data = clean_data(data)

print(data.head())
print("Project is working!")
