#!/usr/bin/python3
for numbers in range(100):
    if numbers < 99:
        print("{:0=2d}, ".format(numbers), end="")
    else:
        print("{}".format(numbers))
