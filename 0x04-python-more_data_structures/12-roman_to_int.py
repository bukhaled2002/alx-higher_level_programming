#!/usr/bin/python3

def roman_to_int(roman_string: str):
    roman_switch = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    n = 0
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if len(roman_string) <= 1:
        return roman_switch.get(roman_string[0])
    for i in range(len(roman_string) - 1):
        if roman_switch[roman_string[i]] >= roman_switch[roman_string[i + 1]]:
            n += roman_switch[roman_string[i]]
        else:
            n -= roman_switch[roman_string[i]]
    n += roman_switch[roman_string[-1]]
    return n
