#!/usr/bin/python3
"""Fetch https://alx-intranet.hbtn.io/status"
import request

if __name__ == "__main__"

request = request.get("https://alx-intranet.hbtn.io./status")
print("Body reponse")
print("\t- type: {}".format(type(request.text)))
print("\t- content: {}".format(request.text))
