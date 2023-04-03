#!/usr/bin/python3
""" This is a Python script that takes a command line argument for a URL,
sends a GET request to the URL using the urllib library, and then prints out the response body as a string.
If the server returns an HTTP error code (e.g. 404 Not Found),
it will print out the error code instead of the response body.
"""

import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
  url_link = sys.argv[1]
  
  request = urllib.request.Request(url_link)
  try:
    with urllib.request.urlopen(request) as response:
      print(response.read().decode("ascii"))
      except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
