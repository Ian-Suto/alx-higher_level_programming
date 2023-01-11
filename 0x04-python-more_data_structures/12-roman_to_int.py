#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
		return None
	list = []
    M = 1000
    D = 500
    C = 100
    L = 50
    X = 10
    V = 5

	for numeral in roman_string:
        if numeral == M:
            list.appen
