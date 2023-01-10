#!/usr/bin/python3
"""Define a file writing function"""


def write_file(filename="", text=""):
    """Write string onto a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        chrs_written = f.write(text)
    return (chrs_written)
