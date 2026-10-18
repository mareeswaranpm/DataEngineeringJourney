import pandas as pd
import sqlite3
print ("loading customer file...")
#read a CSV file into a DataFrame
df = pd.read_csv('data\customer_data.csv')
print("customer_data")
print(df)
#connect to SQLite database
conn = sqlite3.connect('database\customer_data.db')
#Load into SQLite database
df.to_sql("customer_data", conn, if_exists='replace', index=False)
print("\nData loaded into SQLite database.")

#query1

query = """
select * from customer_data where balance > 1500
"""
high_value = pd.read_sql(query,conn)
print("\nHigh Value Customers:")
print(high_value)

#query 2
summary_query = """
select city, count(*) as customer_count, sum(balance) as total_balance, AVG(balance) as average_balance from customer_data group by city
"""
city_summary = pd.read_sql(summary_query,conn)
print("\nCity Summary:")
print(city_summary)
conn.close()
city_summary.to_csv('data\city_summary.csv', index=False)
print("\nCity summary saved to 'data\city_summary.csv'.")

