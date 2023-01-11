#!/usr/bin/python3
"""Define a function that serializes an object to JSON format"""


def class_to_json(obj):
    """Return dictionary description with simple
       data structure for JSON serialization of an object
    """
    return (obj.__dict__)
