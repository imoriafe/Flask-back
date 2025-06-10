import json
import os

DB_FILE = "users.json"

def load_users():
    """Load all users from the JSON file."""
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump([], f)  # ✅ Create empty list in file
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_user(new_user):
    """Add a new user if not already present."""
    users = load_users()
    if any(user["username"] == new_user["username"] for user in users):
        return False  # User exists
    users.append(new_user)
    with open(DB_FILE, "w") as f:
        json.dump(users, f, indent=2)
    return True
