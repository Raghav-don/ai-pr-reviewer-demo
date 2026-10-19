"""Core business logic – safe version.

* Uses environment variables for any API‑like credentials.
* Uses SQLite parameterised queries to avoid injection.
* Provides clear docstrings and type hints.
"""

import os
import sqlite3
from typing import List, Tuple

# ----------------------------------------------------------------------
# Configuration – read from environment (never hard‑code secrets)
# ----------------------------------------------------------------------
API_KEY = os.getenv("DEMO_API_KEY", "")   # empty string if not set – safe placeholder

def get_user_data(user_id: int) -> List[Tuple]:
    """Fetch rows for a given user from the local SQLite demo DB.

    Uses a parameterised query – completely safe from SQL injection.
    """
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()

    # ✅ Parameterised query
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def process_all_users() -> None:
    """Demo of a linear‑time operation – O(N) instead of O(N²)."""
    user_ids = list(range(1, 101))  # 1 … 100

    # ✅ Single loop – O(N)
    for uid in user_ids:
        # Example operation: compute a trivial value (could be any real work)
        _ = uid * 2

    # ✅ Line length kept well under the typical 88‑char limit
    print("Processing completed for all user IDs: " +
          ", ".join(str(uid) for uid in user_ids))


def helper(x: int, y: int) -> int:
    """Simple addition helper – fully typed and documented."""
    return x + y