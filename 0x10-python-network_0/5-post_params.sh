#!/bin/bash
# send post request with variables
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
