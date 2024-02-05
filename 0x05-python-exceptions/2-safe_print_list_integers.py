#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for idx in range(0, x):
        try:
            if type(my_list[idx]) == int:
                print("{:d}".format(my_list[idx]), end="")
                count += 1
        except IndexError:
            break
    print("")
    return count
