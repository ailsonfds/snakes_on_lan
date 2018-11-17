# SNAKES GAME
# Use ARROW KEYS to play, SPACE BAR for pausing/resuming and Esc Key for exiting

# import snake
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint


curses.initscr()
# curses.start_color()
# curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)
crash=False

key = KEY_RIGHT                                                        # Initializing values
score = 0

snake1 = [[4,10], [4,9], [4,8]]                                        # Initial snake co-ordinates
food = [10,20]                                                         # First food co-ordinates
snakes = {'player1':snake1}
win.addch(food[0], food[1], '*')                                       # Prints the food

while key != 27:                                                       # While Esc key is not pressed
    win.border(0)
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')                    # Printing 'Score' and
    win.addstr(0, 27, ' SNAKE ')                                       # 'SNAKE' strings
    win.timeout(150 - (len(snakes)/5 + len(snakes)/10)%120)            # Increases the speed of Snake as its length increases
    for player, snk in  snakes.items():
        prevKey = key                                                  # Previous key pressed
        event = win.getch()
        key = key if event == -1 else event 


        if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
            key = -1                                                   # one (Pause/Resume)
            while key != ord(' '):
                key = win.getch()
            key = prevKey
            continue

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
            key = prevKey

        # Calculates the new coordinates of the head of the snake. NOTE: len(snake) increases.
        # This is taken care of later at [1].
        snk.insert(0, [snk[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snk[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

        # If snake crosses the boundaries, make it enter from the other side
        if snk[0][0] == 0: snk[0][0] = 18
        if snk[0][1] == 0: snk[0][1] = 58
        if snk[0][0] == 19: snk[0][0] = 1
        if snk[0][1] == 59: snk[0][1] = 1

        # Exit if snake crosses the boundaries (Uncomment to enable)
        if (snk[0][0] <= 0) or (snk[0][0] >= 19) or (snk[0][1] <= 0) or (snk[0][1] >= 59): crash=True;break

        # If snake runs over itself
        if snk[0] in snk[1:]: crash=True;break

        
        if snk[0] == food:                                            # When snake eats the food
            food = []
            score += 1
            while food == []:
                food = [randint(1, 18), randint(1, 58)]                 # Calculating next food's coordinates
                if food in snk: food = []
            win.addch(food[0], food[1], '*')
        else:    
            last = snk.pop()                                          # [1] If it does not eat the food, length decreases
            win.addch(last[0], last[1], ' ')
        # win.addch(snk[0][0], snk[0][1], '#', curses.color_pair(1))
        win.addch(snk[0][0], snk[0][1], '#')
    if crash:
        break
    
curses.endwin()
print("\nScore - " + str(score))
print("http://bitemelater.in\n")
