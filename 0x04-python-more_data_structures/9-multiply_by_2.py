#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    _keys = list(new_dir.keys())

    for i in _keys:
        new_dir[i] *= 2

    return (new_dir)
