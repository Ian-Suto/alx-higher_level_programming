#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence == '':
        first = None
        return length, first
    else:
        first = sentence[0]
        return length, first
