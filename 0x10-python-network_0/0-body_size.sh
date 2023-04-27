#!/bin/bash
# Displays the size of body of the response message in bytes
curl -sSL -w "%{size_download}\n" -o /dev/null "$1" 
