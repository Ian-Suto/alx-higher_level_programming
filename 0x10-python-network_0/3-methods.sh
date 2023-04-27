#!/bin/bash
# display all HTTP methods the server will accept
curl -sI "$1" | grep -i allow | grep -o -P '(?<=Allow: )[A-Z, ]+'
