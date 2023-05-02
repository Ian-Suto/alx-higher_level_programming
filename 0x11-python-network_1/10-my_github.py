#!/usr/bin/python3
"""Script that takes GitHub credentials
and uses the GitHub API to display the user id
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    response = get(url, auth=auth.HTTPBasicAuth(user, password))
    print(response.json().get('id'))
