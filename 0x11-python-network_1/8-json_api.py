#!/usr/bin/python3
"""script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""
import requests
import sys


if __name__ == "__main__":
    data = {'q': ""}

    try:
        data['q'] = sys.argv[1]
    except Exception as ex:
        pass

    response = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        json_data = response.json()
        if not json_data:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    except Exception as ex:
        print("Not a valid JSON")
