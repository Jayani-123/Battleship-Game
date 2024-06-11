"""
Battleship Program
This program made to  play game
"""

__author__ = "Jayani Edirisinghe"
__version__ = "2 June 2024"


import numpy as np
from ship import Ship
from board import Board
from player import Player
from dataclasses import dataclass, field

 
def play_game():
    
    MAX_SHIP_HIT = 10 # Number of Hits to win the the Game

    player_board: np.ndarray             #Computers board
    used_cell_player: list[tuple] = []   #To store ships used cells
    player_target_cell: list[tuple] = [] #To store player targets of the board
    player_ship_hits: int = 0            #To store number of success hits by the player
    player_list: list[Player] = []       #To store the player objects
    level: int = 0                       #To store game level
    game_continue :bool = True           #To check to game contiune or not
    
    #Creating list of class ships objects
    ships:list[Ship] = [Ship('Carrier', 5, 'C'),
                        Ship('Battleship', 4, 'B'),
                        Ship('Cruiser', 3, 'R'),
                        Ship('Submarine', 3, 'S'),
                        Ship('Destroyer', 2, 'D')
                        ]
    
        
    level = game_level() #getting the level of the game
    
    #Displaying the board 
    board = Board() 
    board.display_board(board.create_board())
    
    #Adding players to player list
    for player_num in range(1, 3):
        player_board = board.create_board()
        player = Player(player_board, player_target_cell, player_ship_hits, used_cell_player, player_num ) 
        player_list.append(player)

    #Introduction of ships to be place.
    game_intro(ships)    
    board.display_board(board.create_board())
        
    #Place all the ships of the players on the board.
    for i in range(0, 2):
        player_list[i].place_all_ships(ships)  
    
    #Showing the players board.
    for i in range(0, 2):  
        print(f"Player {player_list[i].player_num} Board")
        board.display_board(player_list[i].board)
 
    #Display message to start the battle.
    divide_section()
    print("############## Start the Battle  ############")
    
    #starting to play the game
    while (game_continue):
        for i in range(0, 2):
            player_list[i].player_ship_hits = player_list[i].players_target_postions(level)
            print(player_list[i].player_ship_hits)

        #Displaying players board.
        print("Player1 Board"  ) 
        board.display_board(player_list[0].board)   
        print("Player2 Board")     
        board.display_board(player_list[1].board)                                                  
        
        game_continue = check_winner(MAX_SHIP_HIT, player_list[0].player_ship_hits, player_list[1].player_ship_hits)               
 
       
def check_winner(MAX_SHIP_HIT, player1_ship_hits, player2_ship_hits) -> bool:
    """Checking who is the winner.
    """
    game_continue: bool = True #To check whether to game continue or not
    
    if player1_ship_hits == MAX_SHIP_HIT and player1_ship_hits > player2_ship_hits:
        display_banner('win')
        game_continue = False
    elif player2_ship_hits == MAX_SHIP_HIT and player1_ship_hits < player2_ship_hits:
        display_banner('loss')
        game_continue = False
    elif player2_ship_hits == MAX_SHIP_HIT and player1_ship_hits == player2_ship_hits:
        display_banner('draw')
        game_continue = False
    else:
        game_continue
    return game_continue
            

def display_banner(winner_msg: str):
    """display who is the winner.
    """
    divide_section()
    match winner_msg:
        case 'win':
            print("            Congratulations !!! You win the Game")
        case 'loss':
            print("            !!! You Loss the Game!!!!!")
        case 'draw':
            print("            !!! Game Draw!!!!!")
    divide_section()
    
    
def divide_section():
    """To divide sections in user display messages"""
    section_seperator: str = '#'
    print(section_seperator*60)
    
    
def game_level():
    """Display game level to choose
    """
    print("Select the level of the game:")
    print("1 - EASY")
    print("2 - MEDIUM")
    print("3 - HARD")
    level  = int(input("Select the level number:"))
    divide_section()
    return level
        
        
def game_intro(ships: list[Ship]):
    """Instruction to place the ship to the player.
    """
    print("To win the game you have to bombed the all the ships")
    print("There are 5 ships to Bomb:")
    print("Type of ships on the board:")
    for item, ship in enumerate(ships):
        print(f"{item + 1}. {ship.name}")    
    divide_section()
    print("Lets place ships on your board:")