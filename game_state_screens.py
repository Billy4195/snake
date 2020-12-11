"""

Filename:     game_state_screens.py
Author:       Kyle Cookerly

Description:  Function for the main menu logo the game option window
              and the game over window

"""

import curses


def draw_start_window(height, width):
    """
    Draws the main logo to the screen
    """
    start_screen = curses.newwin(height, width, 0, 8)
    start_screen.addstr(12, 27, "  ______   ___    _       _       _   __   ______  ")
    start_screen.addstr(13, 27, " / _____\ |   \  | |     / \     | | / /  | _____| ")
    start_screen.addstr(14, 27, " \ \___   | |\ \ | |    /___\    | |/ /   | |___   ")
    start_screen.addstr(15, 27, "  \__  \  | | \ \| |   / \_/ \   |  _ \   | ____|  ")
    start_screen.addstr(16, 27, " ____\  \ | |  \   |  /  ___  \  | | \ \  | |____  ")
    start_screen.addstr(17, 27, " \______/ |_|   \__| /__/   \__\ |_|  \_\ |______| ")

    start_screen.addstr(19, 27, "               Press any key to play               ")
    while True:
        if start_screen.getch() is not None:
            break
    curses.endwin()


def draw_option_select_window():
    """
    Draws the game type option and choices to the screen
    :return: bool based on the game type selection
    """
    option_screen = curses.newwin(20, 60, 0, 8)
    option_screen.addstr(7, 24,  "Select Game Mode")
    option_screen.addstr(12, 13, "(1) Solid Walls    (2) Pass Through Walls")
    key_pressed = None
    while True:
        key_pressed = option_screen.getch()
        if key_pressed == ord("1") or key_pressed == ord("2"):
            break
    curses.endwin()
    if key_pressed == ord("1"):
        return False
    else:
        return True

def draw_gift_window(height, width):
    content = list()
    with open("gift.dat", "rb") as fp:
        b = fp.read(1)
        while b:
            content.append(int.from_bytes(b, "little") ^ 25)
            b = fp.read(1)

        text = bytearray(content).decode("utf8")
    content = text.split("\n")

    gift_screen = curses.newwin(height, width, 0, 10)
    idx = 0
    for line in content:
        gift_screen.addstr(idx, 10, line)

        idx += 1
    while True:
        if gift_screen.getch() is not None:
            break
    return


def draw_game_over_window(score, height, width):
    """
    Draws the game over message and the user's final score onto the screen
    :param score: Passed in score the user got in that round
    """
    if score >= 500:
        draw_gift_window(height, width)
    else:
        game_over_screen = curses.newwin(height, width, 0, 10)
        game_over_screen.addstr(12, 45, "Game Over")
        game_over_screen.addstr(15, 42, "Final Score: " + str(score))
        game_over_screen.addstr(20, 37, "Press any key to continue")
        while True:
            if game_over_screen.getch() is not None:
                break
    curses.endwin()
    

