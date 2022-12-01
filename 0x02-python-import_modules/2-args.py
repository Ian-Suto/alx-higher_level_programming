#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv)-1 == 0:
        print("0 arguements")
    elif len(argv)-1 == 1:
        print("1 arguement:")
        print("1: {}".format(argv[1]))
    elif len(argv)-1 > 1:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(len(argv)):
            if i == 0:
                continue
            print("{}: {}".format(i, argv[i]))
