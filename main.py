from src.data_ingestion import load_data
from src.visualization_agent import generate_visuals

data = load_data("data/sample_dataset.csv")
generate_visuals(data)
print("EDA visuals generated in reports folder")
