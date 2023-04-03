#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
 - The Letter is sent as the value of the variable
 - If no letter is provided, then it sends q="".
 """
 
import sys
import request

def search_user(letter):
url = "http://0.0.0.0:5000/search_user"
pyaload = {"q": letter}

try:
response = requets.post(url, data=payload).json()
if not response:
print("No results"
else:
print("[{}] {}"/format(response.get("id"), response.get("name)))
except ValueError:
print("Not a valid JSON")

if __name__ == "__main__":
letter = sys.argv[1] if len(sys.argv) > 1 else""
search_user(letter)
