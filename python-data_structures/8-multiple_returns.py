#!/usr/bin/python3
#8-multiple_returns.py


def multiple_returns(sentence):
    """Returns the length of the character and its first character."""
    if sentence =="":
        return (0, None)
    return (len(sentence), sentence[0])
