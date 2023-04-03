#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
"""

import sys
import requests

if __name__ == "__main__":
    url_link = sys.argv[1]

    reqst = requests.get(url_link)
    if reqst.status_code >= 400:
        print("Error code: {}".format(reqst.status_code))
    else:
        print(reqst.text)
