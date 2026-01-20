import sqlite3
from pathlib import Path
import pandas as pd

DB_PATH = Path("app.db")
CSV_PATH = Path("sampledata.csv")

def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
            CREATE TABLE IF NOT EXISTS transactions (
                txn_id INTEGER PRIMARY KEY,
                user_id TEXT NOT NULL,
                property_id TEXT NOT NULL,
                city TEXT NOT NULL,
                state TEXT NOT NULL,
                amount REAL NOT NULL,
                txn_ts TEXT NOT NULL
            )
        """
    )
    conn.commit()

def seed_from_csv(conn: sqlite3.Connection) -> dict:
    init_db(conn)
    cur = conn.execute("SELECT COUNT(*) AS n FROM transactions")
    n = cur.fetchone()['n']

    if n > 0:
        return {"already_seeded": True, "rows_loaded": 0}

    df = pd.read_csv(CSV_PATH)
    # Basic cleaning for demo purposes:
    df["txn_ts"] = pd.to_datetime(df["txn_ts"], errors="raise")
    df["amount"] = pd.to_numeric(df["amount"], errors="raise")

    # Write to SQLite
    df.to_sql("transactions", conn, if_exists="append", index=False)

    return {"already_seeded": False, "rows_loaded": int(df.shape[0])}
