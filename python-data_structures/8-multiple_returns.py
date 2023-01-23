#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        tuple_return = (0, None)
        return tuple_return
    tuple_return = (len(sentence), sentence[0])
    return tuple_return
