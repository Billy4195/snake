"""

Filename:     snake_main.py
Author:       Kyle Cookerly

Description:  Console-based Snake clone, written in Python 3.5.1
              using the curses module.

"""
import curses                                  # For terminal control
from game import Game
from game_state_screens import draw_start_window, draw_game_over_window, draw_option_select_window


curses.initscr()                                # Starts screen
curses.noecho()                                 # Hides the keyboard input from the terminal
curses.curs_set(0)

WIN_HEIGHT = 30
WIN_WIDTH = 100

def main():
    draw_start_window(WIN_HEIGHT, WIN_WIDTH)
    snake_game = Game(True, height=WIN_HEIGHT, width=WIN_WIDTH)

    while not snake_game.is_game_over():
        snake_game.run_game()

    snake_game.end_window()
    draw_game_over_window(snake_game.get_game_score(), WIN_HEIGHT, WIN_WIDTH)

if __name__ == "__main__":
    main()
