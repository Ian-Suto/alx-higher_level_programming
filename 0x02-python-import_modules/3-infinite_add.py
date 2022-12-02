#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add = 0
    i = len(argv) - 1
    if i == 0:
        print("{}".format(i))
    else:
        for j in range(len(argv)):
            if j == 0:
                continue
            add = add + int(argv[j])
        print("{}".format(add))
