from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

with DAG(
    dag_id="create_stock_table",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    create_stock_table = PostgresOperator(
    task_id="create_stock_table",
    postgres_conn_id="postgres",
    sql="""
        CREATE TABLE IF NOT EXISTS stock_prices (
            symbol TEXT NOT NULL,
            timestamp TIMESTAMP NOT NULL,
            open NUMERIC,
            high NUMERIC,
            low NUMERIC,
            close NUMERIC,
            volume BIGINT,
            PRIMARY KEY (symbol, timestamp)
        );
        """
    )