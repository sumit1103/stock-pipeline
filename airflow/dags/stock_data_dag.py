from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from fetch_stock_data import run   # ✅ correct

with DAG(
    dag_id="stock_data_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    fetch_task = PythonOperator(
        task_id="fetch_stock_data",
        python_callable=run
    )
