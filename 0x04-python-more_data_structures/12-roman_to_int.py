#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}
    dex_number,prev_number = 0,0
    if not isinstance(roman_string,str) or not roman_string:
        return 0
    for num in reversed(roman_string):
        number = roman_num.get(num, 0)
        if number > prev_number:
            dex_number += number
        else:
            dex_number -= number
    return dex_number
