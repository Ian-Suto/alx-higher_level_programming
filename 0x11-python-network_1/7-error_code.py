#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys


if __name__ == "__main__":
    res_msg = requests.get(sys.argv[1])
    response = res_msg.status_code
    if response >= 400:
        print(f"Error code: {response}")
    else:
        print(res_msg.text)
