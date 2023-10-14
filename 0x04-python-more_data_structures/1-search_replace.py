#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def new_function(item):
        return replace if item == search else item
    return list(map(new_function, my_list))
