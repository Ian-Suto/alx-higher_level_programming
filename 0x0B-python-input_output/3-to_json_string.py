#!/usr/bin/python3
import json
"""Get JSON reperenstation of a string"""


def to_json_string(my_obj):
    """Convert string to JSON representation"""
    json_string = json.dumps(my_obj)
    return (json_string)
