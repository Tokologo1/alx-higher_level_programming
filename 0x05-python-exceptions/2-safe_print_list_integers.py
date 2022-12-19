#!/usr/bin/python3
def safe_print_lisy_integers(my_List=[], x=0):
    count = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end='')
            count +=1
        except (TypeError, ValueError):
            pass
        print()
        return count
