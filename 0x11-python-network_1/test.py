#!/usr/bin/python3
import urllib.request
import sys

response = urllib.request.urlopen(sys.argv[1])

header = response.getheaders()
for h in header:
    if 'X-Request-Id' in h[0]:
        value = h[1]
        print(value)
response.close()

