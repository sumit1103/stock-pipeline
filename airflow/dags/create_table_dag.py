from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

with DAG(
    dag_id="create_stock_table",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    create_table = PostgresOperator(
        task_id="create_stock_table",
        postgres_conn_id="postgres_default",
        sql="sql/create_stock_table.sql",
    )
