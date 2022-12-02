#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv) - 1
    if i == 0:
        print("{} arguments.".format(i))
    else:
        if i == 1:
            print("{} argument:".format(i))
        else:
            print("{} arguments:".format(i))
        for j in range(len(argv)):
            if j == 0:
                continue
            print("{}: {}".format(j, argv[j]))
