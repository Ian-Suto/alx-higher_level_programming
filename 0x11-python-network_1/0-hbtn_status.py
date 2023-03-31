#!/usr/bin/python3
"""Fetch https://intranet.hbtn.io/status specifying output."""
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as res_msg:
        response = res_msg.read()
        print("Body reponse:")
        print("\t- type: {}".format(type(response)))
        print(f"\t- content: {response}")
        print("\t- utf8 content: {}".format(response.decode("utf-8")))
