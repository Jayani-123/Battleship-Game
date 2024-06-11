"""
Battleship Program
This program have the attributes and methods related to player
"""


__author__ = "Jayani Edirisinghe"
__version__ = "2 June 2024"


import numpy as np
import random
from dataclasses import dataclass,field
from ship import Ship 


@dataclass  
class Player:  

    board: np.ndarray                                     #players board  
    target_cell: list     = field(default_factory = list) #To store player all the targets of the board
    ship_hits: int        = 0                             #To store number of success hits by the player
    used_cell_ships: list = field(default_factory = list) #To store ships used cells
    player_num: int       = 0                             #To store the player number
    hit_targets: list     = field(default_factory = list) #To store hit targets
    missed_targets: list  = field(default_factory = list) #To store missed targets
    
        
    def place_all_ships(self, ships: list[Ship]):
        """Placing the ships
        """
        for ship in ships:
            self.used_cell_ships = ship.place_ship(self.board, self.used_cell_ships, self.player_num)
    
    
    def ship_target(self, row: int,col: int)->int:
        """To capture missile targets
        """
        MISSED :str      = 'M' #To show missed target  
        SUCCESSFUL :str  = 'X' #To show successful targets 
        
        #checking the cell value on the board
        if self.board[row][col] == "." :
            print("Missed the ship")
            self.board[row][col] = MISSED 
            self.ship_hits += 0
            self.missed_targets.append((row,col))  
            print(f"Missed Targets:{self.missed_targets}")
        elif self.board[row][col] == MISSED  or self.board[row][col] == SUCCESSFUL:
            print("Already used cell")
        else:
            print("shipped bombed")
            self.ship_hits += 1
            self.board[row][col] = SUCCESSFUL
            self.hit_targets.append((row,col)) 
            print(f"Bombed Targets:{self.hit_targets}") 
            
        new_targets = (row,col)
        self.target_cell.append(new_targets)
    
        return  self.ship_hits
        
        
    def get_target_position(self ):
        """Taking Targets from the user
        """
        try:
            print("Lets Hit The Ship please give position for the targets:")
            row = int(input("Enter (0-9) x cordinates of the target position: "))
            col = int(input("Enter (0-9) y cordinates of the target position: "))
            return self.ship_target(row, col )
            
        except ValueError as error:
            #Handling the users incorrect input
            print(f"Please enter valid input to target to the ships.{error}")
            return self.ship_hits
        
        except IndexError as error:
            print(f"Please enter value in range 0 to 9 {error}")
            return self.ship_hits 
        
                
    def generate_random_cell(self):
        """Random generation of row and col to bomb the bot ships for Easy Level
        """
        already_used = True 
        indices =  np.random.randint(0, high = 10, size = 2)  # Making pair of random integers between 0 and 10 (exclusive)     
        row = indices[0] #storing random number as row
        col = indices[1] #storing random number as coloumn
        
        #checking row ,col already used for targets
        while(already_used):
            if (row,col) not in self.target_cell:
                already_used = False
                return row,col
            else:
                indices =  np.random.randint(0, high=10, size=2)  # Making pair of random integers between 0 and 10 (exclusive)     
                row = indices[0] #storing random number as row
                col = indices[1] #storing random number as column

    
    def generate_bot_cell_medium(self):
        """Random generation of row and col to bomb the bot ships for Medium Level.
        """
        possible_targets:list[tuple]  = []  #To store possible targets for bot
        bot_guess:list[tuple] = []          #To store bot guesses
        row, col = self.generate_random_cell()
            
        if self.ship_hits > 0:
            (row, col) = self.hit_targets[-1] #Storing the last hit row and col
            print(row,col)
            possible_targets = [(row + 1, col),(row - 1, col),(row, col - 1),(row, col + 1)]
            for (new_target_row, new_target_col) in possible_targets:
                if 0 <= new_target_row < 10 and 0 <= new_target_col < 10 and (new_target_row, new_target_col) not in self.target_cell:
                    bot_guess.append((new_target_row, new_target_col))

            if len(bot_guess) > 0:
                row, col = bot_guess.pop()
            else:
                row, col = self.generate_random_cell() 
                
        return row, col
    
    
    def generate_cell_hard(self):
        """Begin to guess according to ship sizes.
        """
        already_used: bool = True  #To check target already used
        
        ship_size = [5, 4, 3, 2] #To store ship sizes
   
        indices =  np.random.randint(0, high = 10, size = 2)  # Making pair of random integers between 0 and 10 (exclusive)     
        row = indices[0] #storing random number as row
        col = indices[1] #storing random number as coloum
        
        while(already_used):
            for  size in  ship_size:
                #To check pattern of the board 
                if (row + col) % size == 0 and (row, col) not in self.target_cell:
                    already_used = False
                    return row, col
                else:
                    indices =  np.random.randint(0, high = 10, size = 2)  # Making pair of random integers between 0 and 10 (exclusive)     
                    row = indices[0] #Storing random number as row
                    col = indices[1] #Storing random number as coloum
                    
   
    def generate_bot_cell_hard(self):
        """Random generation of row and col to bomb the bot ships for Hard Level.
        """
        possible_targets: list[tuple] = []   #To store possible targets for bot
        bot_guess: list[tuple] = []          #To store bot guesses
        row, col = self.generate_cell_hard() 
        
        #Checking whether there is a ship hit
        if self.ship_hits > 0:
            (row, col) = self.hit_targets[-1] #Storing the last hit row and col
            possible_targets = [(row + 1, col),(row - 1, col),(row, col - 1),(row, col + 1)]
            for (new_target_row, new_target_col) in possible_targets:
                #Checking target is inside the board and not in target_cell list
                if 0 <= new_target_row < 10 and 0 <= new_target_col < 10 and (new_target_row, new_target_col) not in self.target_cell:
                    bot_guess.append((new_target_row, new_target_col))
            #checking bot_guess list is not empty
            if len(bot_guess)>0:
                row, col = bot_guess.pop()
            else:
                row, col = self.generate_cell_hard()
                
        return row, col
        
        
    def bot_target_position(self, level):
        """Computer targets to bomb the player ships for different levels.
        """
        #Checking the level of the game
        if level == 1:
            row, col = self.generate_random_cell()
            return self.ship_target(row, col)
        elif level == 2 :
               row, col = self.generate_bot_cell_medium()
               return self.ship_target(row, col)
        else:
            row, col = self.generate_bot_cell_hard()
            return self.ship_target(row, col)
            
            
    def players_target_postions(self, level)->int:
        """Choosing the target method according to player.
        """
        
        if self.player_num == 2:
            print("------------------Bot Targets------------------")
            self.bot_target_position(level) 
        else:
            print("------------------Player Targets------------------")
            self.get_target_position()
            
        return self.ship_hits    
                 


            

            
        
        