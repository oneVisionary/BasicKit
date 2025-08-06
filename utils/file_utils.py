import json
import os

def load_json(filepath, default=None):
    if not os.path.exists(filepath):
        return default if default is not None else {}
    
    with open(filepath, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return default if default is not None else {}
        
def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
   