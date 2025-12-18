import yfinance as yf
import psycopg2
from psycopg2.extras import execute_values

DB_CONFIG = {
    "dbname": "airflow",
    "user": "airflow",
    "password": "airflow",
    "host": "postgres",
    "port": 5432,
}

def fetch_stock_data(symbol: str, period="1mo", interval="1d"):
    """
    Fetch OHLCV stock data using yfinance
    """
    ticker = yf.Ticker(symbol)
    df = ticker.history(period=period, interval=interval)

    if df.empty:
        raise ValueError(f"No data returned for symbol {symbol}")

    df = df.reset_index()
    df["symbol"] = symbol

    return df[["symbol", "Date", "Open", "High", "Low", "Close", "Volume"]]

def store_data(df):
    """
    Store stock data into PostgreSQL (idempotent, batch insert)
    """
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # Create table once (safe to keep here)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS stock_prices (
            symbol TEXT,
            timestamp TIMESTAMP,
            open NUMERIC,
            high NUMERIC,
            low NUMERIC,
            close NUMERIC,
            volume BIGINT,
            PRIMARY KEY (symbol, timestamp)
        );
    """)

    records = [
        (
            row.symbol,
            row.Date.to_pydatetime(),
            float(row.Open),
            float(row.High),
            float(row.Low),
            float(row.Close),
            int(row.Volume),
        )
        for row in df.itertuples(index=False)
    ]

    execute_values(
        cur,
        """
        INSERT INTO stock_prices
        (symbol, timestamp, open, high, low, close, volume)
        VALUES %s
        ON CONFLICT DO NOTHING;
        """,
        records
    )

    conn.commit()
    cur.close()
    conn.close()

def run():
    """
    Entry point for Airflow PythonOperator
    """
    symbols = ["MSFT", "AAPL", "GOOG"]

    for symbol in symbols:
        df = fetch_stock_data(symbol)
        store_data(df)