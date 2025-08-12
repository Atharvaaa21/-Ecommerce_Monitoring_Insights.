import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# Load dataset (replace with your local path or S3 URL)
df = pd.read_csv('data/olist_orders_dataset.csv')

# Clean data
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])

# Connect to MySQL
engine = create_engine('mysql+mysqlconnector://root:password@localhost/ecommerce')

# Load into MySQL
df.to_sql('orders', engine, if_exists='replace', index=False)
print("Data loaded successfully into MySQL.")
