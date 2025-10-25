"""
Output Handler Module
---------------------
Handles saving documentation, JSON data, and logs to the 'output' folder.
"""

import os
import json 
from datetime import datetime


OUTPUT_ROOT = "output"
DOCS_PATH = os.path.join(OUTPUT_ROOT, "docs")
DATA_PATH = os.path.join(OUTPUT_ROOT, "data")
LOGS_PATH = os.path.join(OUTPUT_ROOT, "logs")

for path in [DOCS_PATH, DATA_PATH, LOGS_PATH]:
    os.makedirs(path, exist_ok=True)

def save_json(data, filename):
    """Save any dictionary/list data as a JSON file."""
    file_path = os.path.join(DATA_PATH, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {file_path}")

def save_markdown(content, filename):
    """Save generated documentation as Markdown file."""
    file_path = os.path.join (DOCS_PATH, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Documentation saved to {file_path}")

def log_message(message):
    """Log system progress or errors into a timestamped file."""
    os.makedirs(LOGS_PATH, exist_ok=True)
    log_file = os.path.join(LOGS_PATH, "generation_log.txt")

    timesatamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    entry = f"{timesatamp} {message}\n"

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(entry)

    print(f"{entry.strip()}")
