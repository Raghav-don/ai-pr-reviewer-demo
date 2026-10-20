#!/usr/bin/env python3
"""
Test file with intentional security and code quality issues.
This file is designed to trigger both PR-Agent and CodeQL findings.
"""

import os
import sys
import subprocess
import hashlib
import sqlite3
import pickle
from typing import List, Dict


# Issue 1: Hardcoded secret (CodeQL: hardcoded-credentials)
API_KEY = "sk-live-1234567890abcdefghijklmnopqrstuvwxyz"
DATABASE_PASSWORD = "super-secret-password-123"


# Issue 2: SQL Injection vulnerability (CodeQL: sql-injection)
def get_user_by_name(username: str) -> List[Dict]:
    """Get user by name - VULNERABLE to SQL injection."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Direct string interpolation - SQL injection!
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()


# Issue 3: Command injection (CodeQL: command-injection)
def ping_host(host: str) -> str:
    """Ping a host - VULNERABLE to command injection."""
    # User input directly in shell command
    result = subprocess.run(f"ping -c 4 {host}", shell=True, capture_output=True, text=True)
    return result.stdout


# Issue 4: Insecure deserialization (CodeQL: deserialization-of-untrusted-data)
def load_user_data(data: bytes) -> Dict:
    """Load user data - VULNERABLE to pickle deserialization attack."""
    return pickle.loads(data)


# Issue 5: Weak cryptographic hash (CodeQL: weak-cryptographic-hash)
def hash_password(password: str) -> str:
    """Hash password using weak MD5."""
    return hashlib.md5(password.encode()).hexdigest()


# Issue 6: Path traversal (CodeQL: path-traversal)
def read_file(filename: str) -> str:
    """Read file - VULNERABLE to path traversal."""
    base_path = "/var/www/files/"
    # No validation - can read arbitrary files
    full_path = base_path + filename
    with open(full_path, "r") as f:
        return f.read()


# Issue 7: Missing docstring and type hints (PR-Agent: code quality)
def process_items(items):
    total = 0
    for item in items:
        total += item.value
    return total


# Issue 8: Mutable default argument (PR-Agent: bug)
def add_item(item, items=[]):
    items.append(item)
    return items


# Issue 9: Broad exception handling (PR-Agent: error handling)
def risky_operation():
    try:
        return 1 / 0
    except:
        pass  # Swallows all exceptions


# Issue 10: Inefficient loop (PR-Agent: performance)
def find_duplicates(items: List[str]) -> List[str]:
    duplicates = []
    for i, item in enumerate(items):
        if item in items[i+1:]:
            duplicates.append(item)
    return duplicates


# Issue 11: Unused import (PR-Agent: cleanup)
import json
import random
import datetime


# Issue 12: Hardcoded file path (PR-Agent: maintainability)
CONFIG_FILE = "/home/user/config/production.json"


class UserManager:
    """User management class with issues."""
    
    def __init__(self):
        self.users = {}
        # Issue: Hardcoded admin credentials
        self.admin_token = "admin-token-12345"
    
    # Issue: Missing type hints
    def add_user(self, name, email):
        self.users[name] = email
    
    # Issue: SQL injection in method
    def get_user_email(self, name):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        query = f"SELECT email FROM users WHERE name = '{name}'"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0] if result else None


if __name__ == "__main__":
    print("Test file for PR-Agent and CodeQL")
    print(f"API Key: {API_KEY}")