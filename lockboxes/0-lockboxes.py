#!/usr/bin/python3

def canUnlockAll(boxes):
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