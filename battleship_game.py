"""
Battleship Program
This program one player is computer and other player is user 
"""

__author__ = "Jayani Edirisinghe"
__version__ = "2 June 2024"


from play_game import play_game,divide_section


def main():
    
    divide_section()
    print("\nWelcome to the BATTLESHIP GAME\n")
    divide_section()
    
    play_game()
    
    divide_section()
    print("           Game Over  ")
    divide_section()
 
 
if __name__ == "__main__":
    main()
