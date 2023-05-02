#!/usr/bin/python3
"""Script manages urllib.error.HTTPError exceptions and
print: Error code: followed by the HTTP status code"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            the_page = response.read()
            print(the_page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
