#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
"""

import sys
import request

if __name__ == "__main__":
  url_link = sys.argv[1]
  value = {"email": sys.argv[2]}
  
  request = request.post(url, data=value)
  print(request.text)
