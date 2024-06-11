"""
Battleship Program
This program have the attributes and methods related to ship
"""


__author__ = "Jayani Edirisinghe"
__version__ = "2 June 2024"


import numpy as np
import random
from dataclasses import dataclass


@dataclass
class Ship():
#Ship class to create ships
    name: str           #name of the ship
    size: int           #number of cell size of ship
    start_ltr_ship: str #starting letter of the ship

           
    def generate_random_cell(self):
        """Random generation of row and col to place the ships.
        """
        indices: tuple #To store random row ,column on the board
        indices =  np.random.randint(0, high = 10, size = 2)  # Making pair of random integers between 0 and 10 (exclusive)     
        row = indices[0] #storing random number as row
        col = indices[1] #storing random number as coloumn
        return row, col


    def random_direction(self):
        """Direction is selected randomly to store the ships
        if direction = 0 it is vertical if direction=1 horizontal. 
        """
        direction =  random.randint(0, 1)
        return direction
    
    
    def player_given_position(self, player_num:int):
        """Taking the positions of the ships to place on the board.
        """
        if player_num == 1:
            row,col   = self.generate_random_cell() #To store randomly generated row and column
            direction = self.random_direction()   #To store randomly generated direction
        else:
            print(f"Please enter place of the {self.name} ")
            direction = int(input("Enter the direction 0 for vertical 1 for horizontal:")) 
            row       = int(input("Row Position(0-9)    :"))
            col       = int(input("Column Position(0-9) :"))
            
        return row, col, direction
    
    
    def alert_wrong_position(self):
        """Alerting user about invalid position on the board.
        """
        print("!!!Invalid Postion!!!!")
        print("Please provide another position")
        
    
    def place_ship(self, board: np.array, used_cell: list, player_num: int) -> list:
        """
        To place the ship.
        """
        BOARD_SIZE = 10  # To store Board Size
        row, col, direction = self.player_given_position(player_num)
        
        condition = True  # To check row and col are inside the board.
        
        # To place the ship inside the board and checking cell is not already used.
        while condition:
            if direction == 0 and  row <= BOARD_SIZE-self.size and all((row + num, col) not in used_cell for num in range(self.size)):  # Direction is vertical and checking row inside board.
                for num in range(self.size):
                    board[row + num, col] = self.start_ltr_ship
                    used_cell.append((row+num, col))
                condition = False
            elif direction == 1 and  col <= BOARD_SIZE-self.size and all((row, col + num) not in used_cell for num in range(self.size)):  # Direction is horizontal and checking col inside board.
                for num in range(self.size):
                    board[row, col + num] = self.start_ltr_ship
                    used_cell.append((row, col + num))
                condition = False
            else:
                if player_num == 2:
                    self.alert_wrong_position()
                row, col, direction = self.player_given_position(player_num)
        
        return used_cell


