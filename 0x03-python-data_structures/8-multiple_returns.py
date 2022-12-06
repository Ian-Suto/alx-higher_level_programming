#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence:
        first = sentence[0]
        return length, first
    else:
        return None
