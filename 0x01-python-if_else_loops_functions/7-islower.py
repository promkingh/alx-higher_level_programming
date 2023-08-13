#!/usr/bin/python3
def islower(c):
    for a in range(ord('a'), ord('z') + 1):
        if ord(c) == a:
            return (True)
    return (False)
