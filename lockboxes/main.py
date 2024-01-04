#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

if __name__ == "__main__":
  boxes = [[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
  print(canUnlockAll(boxes))