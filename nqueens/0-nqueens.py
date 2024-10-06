#!/usr/bin/python3
'''Solving the N Queens problem'''

import sys


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    sys.exit(1)

if N < 4:
    print('N must be at least 4')
    sys.exit(1)

def printSolution(board):
    """Prints the solution as a list of queen positions"""
    solution = []
    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)

def isSafe(board, row, col):
    """Checks if a queen can be placed at (row, col) without attacks"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

def solveNQUtil(board, col):
    """Utility to solve the N Queens problem recursively"""
    if col == N:
        printSolution(board)
        return True
    res = False
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1) or res
            board[i][col] = 0
    return res

def solveNQ():
    """Driver function to initialize the board and start solving"""
    board = [[0] * N for _ in range(N)]
    solveNQUtil(board, 0)
solveNQ()
