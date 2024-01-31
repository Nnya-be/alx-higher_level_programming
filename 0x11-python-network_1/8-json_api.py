#!/usr/bin/python3
"""
Send a POST request with a letter a s a parameter
"""
import requests
import sys
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) != 2:
        r = requests.post(url, data={'q': ''})
    else:
        r = requests.post(url, data={'q': sys.argv[1]})

    if r.text:
        try:
            json = r.json()
            id = json.get('id')
            name = json.get('name')
            if id and name:
                print("[{}] {}".format(id, name))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    else:
        print("No result")
