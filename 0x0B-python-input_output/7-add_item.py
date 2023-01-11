#!/usr/bin/python3
"""Script adds all arguements to a Python list and save to file"""
import sys
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


with open("add_item.json", 'r+', encoding="utf-8") as f:
    save_to_json_file(sys.argv[1:], f)
    load_from_json_file("add_item.json")
