📈 Dockerized Stock Data Pipeline with Airflow & PostgreSQL
🚀 Project Overview

This project is an end-to-end, Dockerized data pipeline that automatically fetches stock market data using the yfinance API, orchestrates tasks using Apache Airflow, and stores the data in a PostgreSQL database for analytics.

The pipeline is fully automated, reproducible, and designed to demonstrate real-world data engineering concepts such as ingestion, orchestration, storage, and transformation.

🛠️ Tech Stack

Python

Apache Airflow (2.8.1) – workflow orchestration

PostgreSQL – data storage

Docker & Docker Compose – containerization

yfinance – stock market data source

SQL – data validation & analytics

📊 Data Description

The pipeline fetches OHLCV stock data:

Open

High

Low

Close

Volume

Supported Stock Symbols

MSFT (Microsoft)

AAPL (Apple)

GOOG (Google)

🧱 Project Architecture
yfinance API
     ↓
Apache Airflow DAG
     ↓
PythonOperator
     ↓
PostgreSQL Database
     ↓
SQL Analytics Queries

📁 Project Structure
stock-data-pipeline/
│
├── Dockerfile
├── docker-compose.yml
├── .gitignore
├── README.md
│
├── airflow/
│   └── dags/
│       ├── stock_data_dag.py
│       └── fetch_stock_data.py
│
└── postgres/

⚙️ How the Pipeline Works

Airflow DAG runs on a schedule (daily).

DAG executes a PythonOperator.

Python script fetches historical stock data using yfinance.

Data is stored in PostgreSQL with a composite primary key to avoid duplicates.

SQL queries are used to validate and analyze the data.

Logs and retries are handled by Airflow.

▶️ How to Run the Project
1️⃣ Prerequisites

Docker Desktop installed and running

Git installed

2️⃣ Clone the Repository
git clone https://github.com/sumit1103/Dockerized-Data-Pipeline-with-Airflow.git
cd Dockerized-Data-Pipeline-with-Airflow

3️⃣ Build & Start the Services
docker compose up --build

4️⃣ Access Airflow UI

Open browser:

http://localhost:8000


Login Credentials

Username: airflow
Password: airflow

5️⃣ Trigger the DAG (Optional)
docker compose exec airflow-webserver airflow dags trigger stock_data_pipeline

🗄️ Database Validation
Connect to PostgreSQL
docker compose exec postgres psql -U airflow -d airflow

Verify Raw Data
SELECT * FROM stock_prices LIMIT 10;

Example Analytical Query
SELECT
  symbol,
  DATE(timestamp) AS trade_date,
  AVG(close) AS avg_close
FROM stock_prices
GROUP BY symbol, DATE(timestamp)
ORDER BY trade_date DESC;

🔐 Data Integrity

Uses (symbol, timestamp) as PRIMARY KEY

Prevents duplicate records with ON CONFLICT DO NOTHING

Airflow retries tasks on failure

❗ Why yfinance?

Free and widely used

No API key required

No rate-limit exhaustion

Suitable for historical stock data

✅ Key Features

Fully automated ETL pipeline

Dockerized & reproducible

Handles multiple stock symbols

Production-style Airflow setup

Clean GitHub repository (logs ignored)

📌 Future Enhancements (Optional)

Data visualization dashboard

Alerts on DAG failures

Technical indicators (SMA, EMA)

Cloud deployment

🎯 Conclusion

This project demonstrates a complete data engineering workflow:

ingestion → orchestration → storage → analytics

It is suitable for internships, fresher roles, and junior data engineering positions.

👤 Author

Sumit
GitHub: https://github.com/sumit1103
