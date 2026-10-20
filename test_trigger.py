#!/usr/bin/env python3
"""
Test file to trigger PR Agent review.
This file contains some intentional issues for the PR Agent to catch.
"""

import os
import sys

# Issue 1: Unused import
import json
import random

# Issue 2: Hardcoded secret (should be caught by security review)
API_KEY = "sk-test-1234567890abcdef"  # This is a fake key for testing

# Issue 3: Function without docstring
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Issue 4: Potential SQL injection vulnerability (simulated)
def get_user_query(user_input):
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    return query

# Issue 5: Broad exception handling
def read_file_safely(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except:
        return None

# Issue 6: Mutable default argument
def append_item(item, items=[]):
    items.append(item)
    return items

# Issue 7: Inefficient string concatenation in loop
def build_string(words):
    result = ""
    for word in words:
        result += word + " "
    return result.strip()

if __name__ == "__main__":
    print("Test file for PR Agent")
    print(f"Sum: {calculate_sum([1, 2, 3, 4, 5])}")
    print(f"Query: {get_user_query('admin')}")# Trigger
