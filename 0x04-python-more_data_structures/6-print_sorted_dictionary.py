#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dic = sorted(a_dictionary)
    for keys in sort_dic:
        value = a_dictionary[keys]
        print(f"{keys}: {value}")
        
