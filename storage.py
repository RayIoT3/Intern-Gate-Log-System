import json
import os
from datetime import datetime

def get_today_filename():
    """Creates a file name based on today's date so logs are separated daily."""
    today = datetime.now().strftime("%Y-%m-%d")
    return f"gate_logs_{today}.json"

def load_logs():
    """Loads existing logs. If the file is missing or broken, it starts fresh safely."""
    filename = get_today_filename()
    if not os.path.exists(filename):
        return []
    
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, Exception):
        # Handles corrupt files without crashing
        return []

def save_log(data_dict):
    """Saves a check-in or check-out record so it stays persistent after closing."""
    filename = get_today_filename()
    logs = load_logs()
    logs.append(data_dict)
    
    try:
        with open(filename, "w") as file:
            json.dump(logs, file, indent=4)
    except Exception as e:
        print(f"Could not save log: {e}")
