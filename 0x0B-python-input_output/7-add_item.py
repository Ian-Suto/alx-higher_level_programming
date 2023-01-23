#!/usr/bin/python3
"""A script that adds all arguements to a list and saves them to a JSON file"""
import sys
import os

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    file_name = 'add_time.json'
    args_list = []
    if not os.path.isfile(file_name):
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write('[]')
    json_file = load_from_json_file(file_name)
    if (type(json_file) is list) and all(type(i) is str for i in json_file):
        args_list.extend(json_file)
    args_list.extend(sys.argv[1:])
    save_to_json_file(args_list, file_name)