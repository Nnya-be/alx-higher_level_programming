#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    key_list = list(a_dictionary)
    for key in key_list:
        new_dictionary[key] = a_dictionary[key] * 2
    return new_dictionary
