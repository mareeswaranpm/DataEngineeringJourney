import pandas as pd
df = pd.read_csv('data\customer_data.csv')
print("customer_data_original")
print(df)

high_value = df[df["balance"] > 1500]
print("\nHigh Value Customers:")
print(high_value)
# new column
df["balance_category"] = df["balance"].apply(lambda x: "Premium" if x > 2500 else "STANDARD")
print("\nCustomer Data with Balance Category:")
print(df[["name", "balance", "balance_category"]])

#sort
sorted_df = df.sort_values(by="balance", ascending=False)
print("\nSorted Customer Data by Balance: top 5")
print(sorted_df.head(5))

#groupby city
city_summary = df.groupby("city").agg(
    customer_count=pd.NamedAgg(column="name", aggfunc="count"),
    total_balance=pd.NamedAgg(column="balance", aggfunc="sum"),
    average_balance=pd.NamedAgg(column="balance", aggfunc="mean")
).reset_index()
print("\nCity Summary:")
print(city_summary) 

product_summary = (
    df.groupby("product")
      .agg(
          customers=("customer_id", "count"),
          total_balance=("balance", "sum")
      )
      .reset_index()
)

print("\nProduct Summary")
print(product_summary)

city_summary.to_csv(
    "output/city_summary.csv",
    index=False
)

product_summary.to_csv(
    "output/product_summary.csv",
    index=False
)

print("\nReports created")