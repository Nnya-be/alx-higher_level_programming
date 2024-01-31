#!/usr/bin/python3
"""
use the Github API to retrieve my github account id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth
if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
