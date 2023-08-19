#!/usr/bin/python3
def replace_elements(input_list, old_element, new_element):
    new_list = [new_element if item == old_element else item for item in input_list]
    return new_list

