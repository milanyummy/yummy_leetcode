# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:53:29 2020

@author: YummY
"""
board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

findR = False
rPos = []
i = j = 0
capture = 0
for i in range(8):
    for j in range(8):
       if board[i][j] == "R":
            findR = True
            rRow = i
            rLine = j
            break
    if findR == True:
        break
for i in range(rRow - 1, -1, -1):
    if board[i][rLine] == "B":
        break
    elif board[i][rLine] == "p":
        capture += 1
        break        

for i in range(rRow+1, 8, 1):
    if board[i][rLine] == "B":
        break
    elif board[i][rLine] == "p":
        capture += 1
        break  

for j in range(rLine-1, -1, -1):
    if board[rRow][j] == "B":
        break
    elif board[rRow][j] == "p":
        capture += 1
        break

for j in range(rLine+1, 8, 1):
    if board[rRow][j] == "B":
        break
    elif board[rRow][j] == "p":
        capture += 1
        break
print(capture)