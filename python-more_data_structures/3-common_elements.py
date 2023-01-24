#!/usr/bin/python3
def common_elements(set_1, set_2):
#set_3 = [element for element in set_1 if element in set_2]
    set_3 = set(set_1 & set_2)
    return set_3

