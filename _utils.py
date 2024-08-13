import os
import json

from enum import Enum


with open('config.json') as file:
    config = json.load(file)

VIDEO_DIR = config['VIDEO_DIR']
AUDIO_DIR = config['AUDIO_DIR']
PARAMS_JSON_PATH = config['PARAMS_JSON_PATH']

os.makedirs(VIDEO_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)

resolution_map = {
    "SD": "480",
    "HD": "720",
    "FHD": "1080"
}

def json_read(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        return json.load(file)  # Don't use file.read() here

def json_write(json_path, text):
    with open(json_path, 'w') as file:
        json.dump(text, file, indent=4)

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_text_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

class FILE_TYPE(Enum):
    VIDEO = 1
    AUDIO = 2
    JSON = 3

def get_file_from_dir(dir, file_name, file_type):
    files = os.listdir(dir) # List files in the directory

    for file in files:
        if (file_type == file_type.VIDEO and file == f'{file_name}.mp4') or \
            (file_type == file_type.AUDIO and file == f'{file_name}.wav') or \
            (file_type == file_type.JSON and file == f'{file_name}.json'):

            return file
