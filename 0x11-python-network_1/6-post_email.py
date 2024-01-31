#!/usr/bin/python3
"""
send a POST request to an URL
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email_adr = sys.argv[2]
    r = requests.post(url, data={'email': email_adr})
    print(r.text)
