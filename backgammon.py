#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 22:12:48 2021

@author: giuliavoncanal
"""

# ============================================================================ #
# Abgabe Projektarbeit Einführung ins Programmieren mit Python
# 
#     Julia Nierdermeier, Mat.Nr. 
#     Giulia von Canal, Mat.Nr. 2085665
#
#       Keine Note notwendig! 
# ============================================================================ #

import random 


def printBoard(board) :
    
    print("-" * 65)
    print("-" * 65)
    
    for i in range(14) :
        print("||\t", end="")
        
        if i == 0 :
            for j in range(1, 13) :
                
                if j == 7 :
                    print("||\t||\t", end="")
                
                if j < 10 :
                    j = " " + str(j)
                
                print(j, "\t", end="")
                            
        elif i == 13 :
            
            for j in range(13, 25) :
                
                if j == 19 :
                    print("||\t||\t", end="")
                    
                print(j, "\t", end="")
            
        elif i <= 5 : 
            for point in range(1, 13) :
                if point == 7: 
                    print("||\t||\t", end="")
                if not board[point]:
                    print("\t", end="")
                else :
                    if board[point][1] >= i :
                        if board[point][1] >= 5 + i : 
                            if board[point][1] >= 10 + i :
                                print(board[point][0] * 3, "\t", end="")
                            else : 
                                print(board[point][0] * 2, "\t", end="")
                        else : 
                            print("", board[point][0], "\t", end="")
                    else :
                        print("\t", end="")
        
        elif i == 6 or i == 7 :
            print("\t" * 6, end="")
            print("||\t||\t", end="")
            print("\t" * 6, end="")
            
        elif i >= 8 : 
            for point in range(13, 25) :
                if point == 19: 
                    print("||\t||\t", end="")
                if not board[point]:
                    print("\t", end="")
                else :
                    if board[point][1] >= 13 - i :
                        if board[point][1] >= 18 - i : 
                            if board[point][1] >= 23 - i :
                                print(board[point][0] * 3, "\t", end="")
                            else : 
                                print(board[point][0] * 2, "\t", end="")
                        else : 
                            print("", board[point][0], "\t", end="")
                    else :
                        print("\t", end="")
                
        print("||\t")
    
    print("-" * 65)
    print("-" * 65)
        


    
def rollDices() :
    
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    print("")
    
    return [dice1, dice2]

def moveChecker(board, color, start, dest) : 
    
    if board[start] and board[start][0] == color : 
        board[start][1] -= 1
        
        if board[start][1] == 0 : 
            board[start] = []
            
        if not board[dest] : 
            board[dest] = [color, 1]
            
            printBoard(board)
            
        elif board[dest][0] == color :
            board[dest][1] += 1
            
            printBoard(board)
        
        else : 
            if board[dest][1] > 1 : 
                print("You cannot move your checker to", dest)
                print("This point is occupied by the opponent")
            
            else : 
                if color == 'b' :
                    board[-1].append(['w', 1])
                else : 
                    board[-1].append(['b', 1])
                
                board[dest] = [color, 1]
                
                printBoard(board)
                 
    else : 
        print("None of your checkers is on", start)
    
    
    
    
                         
    
       
###################################
###################################

board = {1: ['b', 2], 2: [], 3: [], 4: [], 5: [], 6: ['w', 2],
            7: [], 8: ['w', 3], 9: [],  10: [], 11 : [], 12: ['b',5],
            13: ['w', 2], 14: [], 15: [], 16: [], 17: [], 18: ['b', 5],
            19: [], 20: ['b', 3], 21: [], 22: [], 23: [], 24: ['w', 5], -1 : []}


printBoard(board)

moveChecker(board, 'b', 1, 6)

## game loop 

running = True

while running : 
    
    print("Black's turn.")
    
    result = rollDices()
    print(result[0], result[1]) 
    
    #moveInput = input()

    #test2






#testtest