#!/usr/bin/python3
"""Script to fetch https;//alx/intranet.hbtn.io/status."""
import urllib.request

if __name__ == "__main__":
    request_test = urllib.request.Request)"https://alx-intranet.hbtn.io./status")
    with urllib.request.urlopen(request) as reposnse:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- cotent: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8)))