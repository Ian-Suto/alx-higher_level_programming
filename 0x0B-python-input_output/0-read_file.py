#!/usr/bin/python3
"""Define a file reading function"""


def read_file(filename=""):
    """Reads a text file (utf-8) and prints it"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
