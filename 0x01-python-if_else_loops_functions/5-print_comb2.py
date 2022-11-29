#!/usr/bin/python3
for i in range(100):
    if i == 0:
        print(f"{i:0>2}", end="")
    else:
        print(f", {i:0>2}", end="")
