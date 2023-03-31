#!/usr/bin/python3
# access a variable's value in the header's response
import urllib.request
import sys


res_msg = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(res_msg) as response:
    value = response.getheader('X-Request-Id')
    print(value)
