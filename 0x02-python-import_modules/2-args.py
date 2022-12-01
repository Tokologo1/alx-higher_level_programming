#/usr/bin/python3

if __name__ == " __main__":
    """Print the number of argument and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count is 0:
        print("{:d} arguments.".format(count))
    elif count is 1:
        print("{:d} argument:".format(count))
    else:
        print("{:d} arguments:".format(count))

        for i in range(count):
            print("{:d}: {:s}".format(i, sys.argv[i]))
