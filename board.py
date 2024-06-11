"""
Battleship Program
This program have the attributes and methods related to board.
"""

__author__ = "Jayani Edirisinghe"
__version__ = "2 June 2024"


import numpy as np
from dataclasses import dataclass


@dataclass  
class Board:
#Board class to create board

    BOARD_SIZE = 10 #To store Board Size


    def create_board(self) -> np.ndarray:
        """
        Creating board of the battleship.
        """
        board = np.empty((self.BOARD_SIZE, self.BOARD_SIZE), dtype = str)

        for cell in range(self.BOARD_SIZE):
            board[cell] = list('.')
        
        return board
    
    
    def display_board(self, board: np.array):
        """
        Display the board of the battleship.
        """
        index:int = -1 #To store the row number of the board
        print("      0    1    2    3    4    5    6    7    8    9")
        for row in board:
            print("   +----+----+----+----+----+----+----+----+----+----+")
            index = index + 1
            if (index != self.BOARD_SIZE):
                print(f"{index} ", end = "")
            else:
                print(f"{index}", end = "")
            for element in row:
                print(f" | {element} ", end = "")            
            print( " |")
        print("   +----+----+----+----+----+----+----+----+----+----+")
         
