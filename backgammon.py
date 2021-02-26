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
from board import *

    
def rollDices() :
    
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    print("Dice rolling...\n")
    
    if dice1 == dice2 : 
        throw = [dice1, dice1, dice1, dice1]
    else : 
        throw = [dice1, dice2]

    for dice in throw : 
        print(dice, end=" ")

    return throw


def inputIsValid(inputStr) : 
    if re.match('(-1|[1-9]|1[0-9]|2[0-4]) - ([1-9]|1[0-9]|2[0-4]|-1)', inputStr): 
        return True
    else : 
        print("Input does not meet required format. Please try again!")
        return False

def makeMove(color, throw) : 

    if color == 'b' : 
        print("Black's turn.")
    else : 
        print("White's turn.")

    numMoves = len(throw)

    for i in range(numMoves) : 

        inputStr = input("\n\nEnter move:\t")
        inputList = inputStr.split(" - ")

        start = int(inputList[0])
        dest = int(inputList[1])

        while not inputIsValid(inputStr) or not board.moveIsPossible(color, start, dest, throw) : 
            inputStr = input("\n\nEnter move:\t")
            inputList = inputStr.split(" - ")

            start = int(inputList[0])
            dest = int(inputList[1])
        
       
        usedThrow = board.moveChecker(color, start, dest)

        throw.remove(usedThrow)

                       
############################################################################################################################################
############################################################################################################################################


## initialize board 
board = Board([(1,['b', 2]), (6, ['w', 5]), (8, ['w', 3]), (12, ['b', 5]), (13, ['w', 5]), (17, ['b', 3]), (19, ['b', 5]), (24, ['w', 2])])


print(board)


## game loop 

running = True

while running : 
    
    throw_black = rollDices()
    makeMove('b', throw_black)
    
    if board.allCheckersBearedOff('b') :
        print("Black has won the game!")
        running = False
        

    throw_white = rollDices()
    makeMove('w', throw_white)

    if board.allCheckersBearedOff('w') :
        print("White has won the game!")
        running = False