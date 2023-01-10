#!/usr/bin/python3
"""Create an object from JSON file"""
import json


def load_from_json_file(filename):
    """Create object from JSON file"""
    with open(filename, 'r')as f:
        obj_created = json.load(f)
        return (obj_created)
