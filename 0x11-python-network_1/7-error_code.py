#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
"""

import sys
import request

if _name__ == "__main__":
  url_link = sys.argv[1]
  
  try:
    response = request.get(url_link)
    response.raise_for_status()
    print(response.text)
  except request.exception.RequestException as e:
    print(f"Error: {e}")
