FROM apache/airflow:2.8.1-python3.8

USER airflow

RUN pip install --no-cache-dir \
    "multitasking<0.0.10" \
    yfinance
