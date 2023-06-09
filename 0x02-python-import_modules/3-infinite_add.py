#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("0")
    else:
        count = 0
        for i in range(1, len(sys.argv)):
            temp = int(sys.argv[i])
            count += temp
        print("{}".format(count))
