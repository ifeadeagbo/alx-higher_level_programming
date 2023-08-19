#!/usr/bin/python3
def number_keys(a_dictionary):
    numb = 0
    _keys = list(a_dictionary.keys())

    for i in _keys:
        numb += 1

    return (numb)
