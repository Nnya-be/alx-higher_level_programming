#!/usr/bin/python3
"""
use the Github API to retrieve my github account id
"""
import requests
import sys
if __name__ == "__main__":
    c = 0
    url = 'https://api.github.com/repos/{}/{}/commits'
    r = requests.get(url.format(sys.argv[2], sys.argv[1]))
    for i in r.json():
        commit = i.get('sha')
        userx = i.get('commit').get('author').get('name')
        print("{}: {}".format(commit, userx))
        c = c + 1
        if c == 10:
            break
