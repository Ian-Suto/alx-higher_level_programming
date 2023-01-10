#!/usr/bin/python3
"""Define a string appending function"""


def append_write(filename="", text=""):
    """Append string onto a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        chrs_written = f.write(text)
        return (chrs_written)
