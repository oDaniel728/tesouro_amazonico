import json

def get_data(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def save_data(path: str, data: dict) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)