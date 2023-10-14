#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        inner_list = []
        for in_element in row:
            inner_list.append(in_element ** 2)
        result.append(inner_list)
    return result
