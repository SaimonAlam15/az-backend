import os
import json

def source_secrets(directory):
    file_names = os.listdir(directory)
    secrets = {}
    for file_name in file_names:
        with open(f'{directory}/{file_name}', 'r', encoding='utf-8') as f:
            key = file_name.split('.')[0]
            secrets[key] = json.load(f)
    return secrets