#!/usr/bin/python3
"""Function inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r+', encoding='utf-8') as f:
        for line in f:
            if search_string in line:
                f.write(f"{new_string}\n",new_string)
