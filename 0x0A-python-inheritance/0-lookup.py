#!/usr/bin/python3
def lookup(obj):
    """Return a list of all methods and attributes of the given object"""
    return (list(dir(obj)))
