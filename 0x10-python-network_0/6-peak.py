#!/usr/bin/python3
""" Test function find_peak """


def find_peak(lx):
    """fynction to find peak """
    if not lx:
        return None
    for i in range(len(lx)):
        if lx[0] < lx[i]:
            lx[0] = lx[i]

    return lx[0]
