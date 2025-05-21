# - E T L
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
import psycopg2

# Database connection parameters
DB_NAME = "mwaura_project"
DB_USER = "postgres"
DB_PASSWORD = "@Ryan4404"
DB_HOST = "localhost"
DB_PORT = 5432

#Function to Extract data from the API
def extract():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    return response.json()

# Transform the data into a format suitable for loading into the database
def transform(raw_data):
    transformed_data = []
    for coin, price in raw_data.items():
        transformed_data.append((coin, price["usd"], datetime.now()))
    return transformed_data

#function to load the data into the PostgreSQL database
def load(transformed_data):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    cur = conn.cursor()

    cur.execute("""
        CREATE SCHEMA IF NOT EXISTS crypto_data;
        CREATE TABLE IF NOT EXISTS crypto_data.crypto_prices (
            coin text,
            usd_price NUMERIC,
            timestamp TIMESTAMP
        );
    """)
    # Insert the transformed data into the database
    cur.executemany(
        "INSERT INTO crypto_data.crypto_prices (coin, usd_price, timestamp) VALUES (%s, %s, %s)",
        transformed_data
    )

    conn.commit()
    cur.close()
    conn.close()

# Define the DAG
def etl():
    raw= extract()
    clean = transform(raw)
    load(clean)

with DAG(
    dag_id = "crypto_etl",
    start_date = datetime(2025, 1, 1),
    schedule_interval = "@hourly",
    catchup = False
) as dag:

    run_etl = PythonOperator(
        task_id= "run_etl",
        python_callable = etl
    )

    run_etl
