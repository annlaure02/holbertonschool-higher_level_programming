#!/usr/bin/python3
def roman_to_int(roman_string):

    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    if type(roman_string) != str or roman_string is None:
        return 0

    for i, element in enumerate(roman_string):
        if i != (len(roman_string) - 1) and roman_d[element] \
                < roman_d[roman_string[i + 1]]:
            result -= roman_d[element]
        else:
            result += roman_d[element]
    return result
