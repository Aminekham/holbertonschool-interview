#!/usr/bin/python3
"""
Documentation
"""
def rain(walls):
    """
    Calculating i will explain the algorithm later
    """
    walls_list = []
    c = 0
    for i in range(len(walls)):
        if walls[i] != 0:
            c = 0
            walls_list.append(walls[i])
            for j in range(i + 1, len(walls)):
                if walls[j] == 0:
                    c+= 1
                else:
                    if c != 0:
                        walls_list.append(c)
                    walls_list.append(walls[j])
                    break
    water = 0
    walls_list = walls_list[0:-1]
    i = 0
    while(i < len(walls_list) - 2):
        water += min(walls_list[i], walls_list[i+2]) * walls_list[i + 1]
        i = i + 3
    return water
