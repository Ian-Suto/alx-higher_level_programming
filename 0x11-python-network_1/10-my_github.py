#!/usr/bin/python3
"""Script that takes GitHub credentials
and uses the GitHub API to display the user id
"""
from requests import get
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/users/' + user
    headers = {'Accept': 'application/vnd.github+json',
               'Authorization': 'Bearer ' + passwd}
    response = get(url, headers=headers)
    user_info = json.loads(response.text)
    try:
        print(user['id'])
    except Exception as ex:
        print("None")
