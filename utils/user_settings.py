import json, os

SETTINGS_FILE = "data/users.json"

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {}
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=2)

def get_user_settings(user_id):
    settings = load_settings()
    return settings.get(str(user_id), {})

def update_user_settings(user_id, new_settings):
    settings = load_settings()
    settings[str(user_id)] = new_settings
    save_settings(settings)