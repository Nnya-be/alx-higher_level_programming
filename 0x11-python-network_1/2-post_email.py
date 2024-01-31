#!/usr/bin/python3
"""
sends a POST request to the passed URL with email field.
"""
import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email_adr = sys.argv[2]

    values = {'email': email_adr}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode())
