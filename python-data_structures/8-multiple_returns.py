#!/usr/bin/python3
def multiple_returns(sentence):
    # If the sentence is empty, return 0 and None
    if sentence == "":
        return (0, None)
    # Otherwise, return the length of the sentence and its first character
    return (len(sentence), sentence[0])
