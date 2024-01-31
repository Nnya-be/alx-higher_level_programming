#!/usr/bin/python3
"""
Python script that fetches the intranet url.
"""
from urllib import request
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        with request.urlopen(url) as response:
            content = response.read().decode('utf-8')

            print(f"Body response:")
            print(f"\t- type: {type(content)}")
            print(f"\t- content: {content}")
    except Exception as e:
        print(f"Error: {e}")
