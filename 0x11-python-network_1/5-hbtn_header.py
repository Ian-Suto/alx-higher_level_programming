#!/usr/bin/python3
"""Script that fetches URL and shows the specified variable"""
import requests
import sys


if __name__ == "__main__":
    res_msg = requests.get(sys.argv[1])
    response = res_msg.headers['X-Request-Id']
    print(response)
