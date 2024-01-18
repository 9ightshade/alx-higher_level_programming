#!/usr/bin/python3
import sys

def print_arguments():
    # Get the number of arguments
    num_args = len(sys.argv) - 1

    # Print the number of arguments
    if num_args == 0:
        print("Number of argument(s): .")
    elif num_args == 1:
        print("Number of argument(s): 1, followed by:")
    else:
        print("Number of argument(s): {}, followed by:".format(num_args))

    # Print each argument with its position
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments()
