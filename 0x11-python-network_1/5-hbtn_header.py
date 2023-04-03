#!/usr/bin/python3
"""This is a Python code that sends an HTTP GET request to a specified URL using the requests library,
retrieves the response headers, and prints the value of the X-Request-Id header variable.
"""
import sys
import requests

if __name__ == "__main__":
    url_link = sys.argv[1]

    reqst = requests.get(url_link)
    print(reqst.headers.get("X-Request-Id"))
