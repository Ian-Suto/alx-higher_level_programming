#!/usr/bin/python3
"""Script that fetches URL and shows the specified variable"""
import requests
import sys


if __name__ == "__main__":
    try:
        res_msg = requests.post(sys.argv[1], data={'email': sys.argv[2]})
        print(res_msg.content.decode('utf-8'))
    except Exception as ex:
        pass
