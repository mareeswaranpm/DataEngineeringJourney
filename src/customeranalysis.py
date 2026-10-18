import pandas as pd
#read a CSV file into a DataFrame
df = pd.read_csv('data\customer_data.csv')
print("customer_data")
print(df)

#Business logic
high_value = df[df["balance"] > 1500]
print("High Value Customers:")
print(high_value)

#summary
print("Summary:")
city_summary = (df.groupby("city")["balance"].sum().reset_index())
print("\nCity Summary:")
print(city_summary)
