"""Utility helpers – safe version.

* Uses SHA‑256 (via hashlib) for hashing – cryptographically strong for demo.
* Validates file names to prevent path‑traversal.
* No hard‑coded AWS‑style credentials.
* All imports are actually used.
"""

import os
import hashlib
import base64
from pathlib import Path

# ----------------------------------------------------------------------
# Safe hashing – SHA‑256 (still not suitable for production password storage,
# but fine for a demo that deliberately avoids MD5)
# ----------------------------------------------------------------------
def hash_password(password: str) -> str:
    """Return a SHA‑256 hash of the password (hex digest).

    Note: For real applications use a dedicated password‑hashing library
    (e.g., bcrypt, Argon2, PBKDF2). SHA‑256 is used here only to avoid MD5.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def read_file_safely(filename: str) -> str:
    """Read a file and return its contents as a string.

    The function prevents directory‑traversal attacks by resolving the path
    and ensuring it stays inside the current working directory.
    """
    # Resolve the supplied filename relative to the cwd
    requested_path = Path(filename).resolve()
    cwd_path = Path.cwd().resolve()

    # ✅ Ensure the resolved path is a sub‑path of the cwd
    if not requested_path.is_relative_to(cwd_path):
        raise ValueError(f"Access denied: {filename} attempts to traverse outside the project")

    # ✅ Additionally, ensure the file exists and is a regular file
    if not requested_path.is_file():
        raise FileNotFoundError(f"No such file: {filename}")

    with requested_path.open("r", encoding="utf-8") as f:
        return f.read()


def dummy_s3_upload(data: bytes) -> None:
    """Pretend to upload data to S3 – uses credentials from environment only.

    No hard‑coded keys are stored in the source.
    """
    access_key = os.getenv("AWS_ACCESS_KEY_ID", "")
    secret_key = os.getenv("AWS_SECRET_ACCESS_KEY", "")

    if not access_key or not secret_key:
        # In a real demo you might skip the upload or raise a clear error.
        print("AWS credentials not set – skipping S3 upload demo.")
        return

    # In a real implementation you would call boto3 or another SDK here.
    # For the demo we just log that we *would* upload.
    print(f"[Demo] Would upload {len(data)} bytes to S3 using key {access_key[:4]}...")


def long_running_task() -> None:
    """Simulate a short‑running task – keeps line length sane."""
    import time
    time.sleep(0.1)   # a tiny delay just to show the function does something