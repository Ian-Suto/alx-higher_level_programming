#!/usr/bin/python3
"""Script access a variable's value in the header's response"""
import urllib.request
import sys


if __name__ == "__main__":
    res_msg = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(res_msg) as response:
        value = response.getheader('X-Request-Id')
        print(value)
