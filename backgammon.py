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
import re


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
            
            for j in range(24, 12, -1) :
                
                if j == 18 :
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
            for point in range(24, 12, -1) :
                if point == 18: 
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
    
    print("Dices rolling...\n")
    
    return [dice1, dice2]


def inputIsValid(inputStr) : 
    if re.match('([1-9]|1[0-9]|2[0-4]) - ([1-9]|1[0-9]|2[0-4])', inputStr): 
        return True
    else : 
        print("Input does not meet required format. Please try again!")
        return False


def moveIsPossible(board, color, start, dest) : 

    if (color == 'b' and start > dest) or (color == 'w' and start < dest): 
        print("You cannot move in this direction")
        return False

    if board[start] and board[start][0] == color : 

        if not board[dest] : 
            return True 

        else :

            if board[dest][1] > 1 : 
                print("You cannot move your checker to", dest)
                print("This point is occupied by the opponent")

                return False    
            else :  
                return True
                 
    else : 
        print("None of your checkers is on", start)
        return False 
    


def moveChecker(board, color, start, dest) : 
    
    board[start][1] -= 1
        
    if board[start][1] == 0 : 
        board[start] = []
            
    if not board[dest] : 
        board[dest] = [color, 1]
                 
    elif board[dest][0] == color :
        board[dest][1] += 1
        
    else : 

        if color == 'b' :
            board[-1].append(['w', 1])
        else : 
            board[-1].append(['b', 1])
                
            board[dest] = [color, 1]

    printBoard(board)
                


def makeMove(color) : 

    if color == 'b' : 
        print("Black's turn.")
    else : 
        print("White's turn.")
    
    result = rollDices()
    print(result[0], result[1]) 
    
    inputStr = input("\nEnter move:\t")
    inputList = inputStr.split(" - ")

    while not inputIsValid(inputStr) or not moveIsPossible(board, color, int(inputList[0]), int(inputList[1])) : 
        inputStr = input("\nEnter move:\t")
        inputList = inputStr.split(" - ")
    
    moveChecker(board, color, int(inputList[0]), int(inputList[1])) 
                       
    
       
###################################
###################################

board = {1: ['b', 2], 2: [], 3: [], 4: [], 5: [], 6: ['w', 2],
            7: [], 8: ['w', 3], 9: [],  10: [], 11 : [], 12: ['b',5],
            13: ['w', 5], 14: [], 15: [], 16: [], 17: ['b', 3], 18: [],
            19: ['b', 5], 20: [], 21: [], 22: [], 23: [], 24: ['w', 2], -1 : []}


printBoard(board)

## game loop 

running = True

while running : 
    
    makeMove('b')
    makeMove('w')

    running = False