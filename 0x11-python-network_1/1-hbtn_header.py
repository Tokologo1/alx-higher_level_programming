#!/usr/bin/python3
"""Display the X-Request-Id variable found in the header of the response.
"""

import sys
import urllib.request

if __name__ == "__main__":
  url_link = sys.argv[1]
  
  request = urllib.request.Request(url)
  with urllib.request.urlopen(request) as response:
    print(dict(response.header).get("X-request-Id"))
