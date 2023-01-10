#!/usr/bin/python3
"""Get JSON string reprenstation of an object"""
import json


def from_json_string(my_obj):
    """Return object represented by a JSON string"""
    json_string = json.loads(my_obj)
    return (json_string)
