#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    dic_list = list(a_dictionary)
    for dic_key in dic_list:
        if dic_key == key:
            del(a_dictionary[key])
    return a_dictionary
