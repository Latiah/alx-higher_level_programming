#!/usr/bin/python3
def no_c(my_string):
    sentence = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            sentence += letter
    return sentence
