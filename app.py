import pandas as pd
from fastapi import FastAPI, Query
from pydantic import BaseModel
from datetime import datetime
from db import get_conn, seed_from_csv

app = FastAPI(title="Python API + SQL + Pandas MVP")

conn = get_conn()
seed_info = seed_from_csv(conn)

@app.get("/")
def index():
     return "Welcome to Jackass"

@app.get("/health")
def health():
        return {"status": "ok", "db_seed": seed_info}

@app.get("/transactions")
def list_transactions(
        limit: int = Query(20, ge=1, le=200),
        state: str | None = None,
        min_amount: float | None = Query(None, ge=0),
):
    """
    Returns a list of transactions.

    Demonstrates:
    - Dynamic SQL WHERE clause construction
    - Safe parameter binding (prevents SQL injection)
    - API-style filtering + pagination
    """
    sql = "SELECT * FROM transactions"
    params = []
    where = []
    
    if state:
        where.append("state = ?")
        params.append(state)

    if min_amount is not None:
        where.append("amount >= ?")
        params.append(min_amount)  

    if where:
        sql += " WHERE " + " AND ".join(where)
    
    sql += " ORDER BY txn_ts DESC LIMIT ?"
    params.append(limit)

    rows = conn.execute(sql, params).fetchall()

    return {
         "count": len(rows),
         "data": [dict(r) for r in rows]
    }

@app.get("/user/{user_id}/summary")
def user_summary(user_id: str):
    """
    Returns aggregated transaction metrics for a single user.

    Demonstrates:
    - SQL aggregation
    - GROUP BY
    - Returning summary-level data
    """
    row = conn.execute(
         """
            SELECT
                user_id,
                COUNT(*) AS txn_count,
                SUM(amount) AS total_spend,
                AVG(amount) AS avg_amount,
                MIN(txn_ts) AS first_txn,
                MAX(txn_ts) AS last_txn
            FROM transactions
            WHERE user_id = ?
            GROUP BY user_id
        """,
        (user_id,),
    ).fetchone()

    if not row:
        return {
            "user_id": user_id,
            "txn_count": 0,
            "message": "user not found"
        }
    
    return dict(row)

@app.get("/metrics/top_cities")
def top_cities(limit: int = Query(5, ge=1, le=50)):
    """
    Returns top cities by total transaction volume.

    Demonstrates:
    - Fetching raw data using SQL
    - Performing analytics using Pandas
    - Combining SQL + Pandas (very common data API pattern)
    """

    # Pull only required columns from SQL (avoid SELECT *)
    rows = conn.execute(
        "SELECT city, state, amount FROM transactions"
    ).fetchall()

    # Convert SQL rows into a Pandas DataFrame
    df = pd.DataFrame([dict(r) for r in rows])

    # Group by city and state, then calculate metrics
    out = (
        df.groupby(["city", "state"], as_index=False)
          .agg(
              total_volume=("amount", "sum"),
              txn_count=("amount", "count")
          )
          .sort_values(
              ["total_volume", "txn_count"],
              ascending=[False, False]
          )
          .head(limit)
    )

    # Convert Pandas DataFrame back to JSON-serializable format
    return {
        "limit": limit,
        "data": out.to_dict(orient="records")
    }

class TransactionCreate(BaseModel):
    user_id: str
    property_id: str
    city: str
    state: str
    amount: float
    txn_ts: str | None = None

@app.post("/transactions")
def create_transaction(transaction: TransactionCreate):
    """
    Create a new transaction record.
    
    Demonstrates:
    - POST endpoint with request body
    - Pydantic model validation
    - SQL INSERT with parameter binding
    - Returning the created record
    """
    # Use current timestamp if not provided
    txn_ts = transaction.txn_ts or datetime.now().isoformat()
    
    # Insert the transaction
    cursor = conn.execute(
        """
        INSERT INTO transactions (user_id, property_id, city, state, amount, txn_ts)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (transaction.user_id, transaction.property_id, transaction.city, 
         transaction.state, transaction.amount, txn_ts)
    )
    conn.commit()
    
    # Return the created record with its ID
    return {
        "txn_id": cursor.lastrowid,
        "user_id": transaction.user_id,
        "property_id": transaction.property_id,
        "city": transaction.city,
        "state": transaction.state,
        "amount": transaction.amount,
        "txn_ts": txn_ts
    }
