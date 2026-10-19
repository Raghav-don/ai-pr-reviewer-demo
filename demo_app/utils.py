# demo_app/utils.py
"""Utility helpers – contains a few more issues for PR‑Agent to notice."""

import hashlib

# ✅ Use PBKDF2-HMAC-SHA256 for password hashing
def hash_password(password: str) -> str:
    """Return a salted PBKDF2-HMAC-SHA256 password hash string."""
    salt = os.urandom(16)
    iterations = 600_000
    derived_key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, iterations)
    salt_b64 = base64.b64encode(salt).decode("ascii")
    hash_b64 = base64.b64encode(derived_key).decode("ascii")
    return f"pbkdf2_sha256${iterations}${salt_b64}${hash_b64}"

# ❌ Potential path traversal if `filename` comes from user input
def read_file_safely(filename: str) -> str:
    """Read a file and return its contents as a string.
    
    Note: No validation on `filename` – could allow directory traversal.
    """
    with open(filename, "r") as f:
        return f.read()

# ❌ Hardcoded AWS‑style credential (another secret)
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def dummy_s3_upload(data: bytes) -> None:
    """Pretend to upload data to S3 – uses hardcoded credentials."""
    # In a real app you would never embed keys like this.
    print(f"Uploading {len(data)} bytes to S3 using key {AWS_ACCESS_KEY}")

# ❌ Unused import (style)
import json  # noqa: F401  – we keep it to show an unused import warning

# ❌ Line longer than 88 characters (style)
def long_running_task() -> None:
    """Simulate a long running task by sleeping a lot – just for demo."""
    import time
    # This comment makes the line intentionally long to exceed the style limit.
    time.sleep(5)  # pragma: allowlist secret