#!/bin/bash
# send post request with variables
curl -s -X POST -d "email=test@gmail&subject=I will always be here for PLD" "$1"
