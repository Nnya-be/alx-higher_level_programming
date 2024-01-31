#!/usr/bin/python3
"""
displays the value of a specific header field of the response.
"""
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.info().get('X-Request-Id'))
