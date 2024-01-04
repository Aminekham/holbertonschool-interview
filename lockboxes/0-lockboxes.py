#!/usr/bin/python3
""""
This is a way to solve the canunlockall problem
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes: A list of lists representing boxes and their keys.

    Returns:
    - True if all boxes can be opened, False otherwise.
    """
    visited = [False] * len(boxes)
    visited[0] = True
    stack = [0]

    while stack:
        current = stack.pop()

        for key in boxes[current]:
            if 0 <= key < len(boxes) and not visited[key]:
                visited[key] = True
                stack.append(key)

    if False in visited:
        return False
    return True

