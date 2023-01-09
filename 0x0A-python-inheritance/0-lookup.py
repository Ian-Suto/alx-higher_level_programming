#!/usr/bin/python3
"""Defines a method lookup"""


def lookup(obj):
    """Return a list of all methods and attributes of the given object"""
    return (dir(obj))
