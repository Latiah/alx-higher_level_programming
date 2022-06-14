#!/usr/bin/python3
def multiple_returns(sentence):
    character = None
    if sentence:
        character = sentence[0]
    length = len(sentence)
    return (length, character)
