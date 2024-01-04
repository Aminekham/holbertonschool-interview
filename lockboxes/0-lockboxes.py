#!/usr/bin/python3
""""
This is a way to solve the canunlockall problem
"""


def canUnlockAll(boxes):
    """
    idea: collecting all the found keys and intrepret 
    if we can open all the boxes by following any giving 
    way or not
    comparaison is the key to verify those keys
    """
    keys_for_now = []
    c = 1
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            key = boxes[i][j]
            if key not in keys_for_now:
                keys_for_now.append(key)
                c = c + 1
        if c == len(boxes):
            return(True)
    return(False)