import pandas as pd
from pathlib import Path
raw_file = Path("data/raw/customer_data.csv")
df = pd.read_csv(raw_file)

#silver layer
df = df.drop_duplicates()

silver_file = Path("data/silver/customer_data_clean.csv")
df.to_csv(silver_file, index=False)

#gold layer
summary = df.groupby("city")["balance"].sum().reset_index()
gold_file = Path("data/gold/city_summary.csv")
summary.to_csv(gold_file, index=False)
print("Data Lake Pipeline executed successfully. Silver and Gold layers created.")