#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    value_list = a_dictionary.values()
    max_value = max(value_list)
    for key in a_dictionary:
        if a_dictionary[key] == max_value:
            return key
