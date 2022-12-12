#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key in a_dictionary:
        new_dictionary.update({key: a_dictionary[key]})
    for new_key in new_dictionary:
        new_dictionary[new_key] = new_dictionary[new_key] * 2
    return new_dictionary
