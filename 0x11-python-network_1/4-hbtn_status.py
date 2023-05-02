#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    res_msg = requests.get(url)
    response = res_msg.text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
