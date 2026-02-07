from src.data_ingestion import load_data

data = load_data("data/sample_dataset.csv")
print(data.head())
