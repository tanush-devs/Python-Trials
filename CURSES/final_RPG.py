import copy
import curses
import curses.textpad
import time

MAZE = [
    "#############################################",
    "#...#.......#.......#.......#.......#......T#",
    "#.###.#####.#.#####.#.#####.#.#####.#####.#.#",
    "#.#...#...#.#...#...#.....#.#.#...#.#.....#.#",
    "#.#.###.#.#.###.#.#######.#.#.#.#.#.#.#####.#",
    "#.#...#.#.#...#.#...T...#.#...#.#.#.#.#...#.#",
    "#.###.#.#.###.#####.###.#######.#.#.###.#.#.#",
    "#...#.#.#...#.....#...#.#.....#.#.#...#.#.#.#",
    "###.#.#.###.#####.###.#.#.###.#.#.###.#.#.#.#",
    "#...#.#...#.#...#...#.#.#.#.#.#...#...#.#.#.#",
    "#T###.###.#.#.#.###.#.#.#.#.#.#####.###.#.#.#",
    "#.#.....#.#.#.#...#.#.#.#.#.#.....#...#.#.#.#",
    "#.#.#####.#.#.###.#.#.#.#.#.#####.###.#.#.#.#",
    "#.#.#.....#.#...#.#...#.#.#.#.....#...#.#.#.#",
    "#.#.#.#####.###.#.#####.#.#.#.#####.###.#.#.#",
    "#.#.#...#...#...#.....#.#.#.#.#...#...#.#.#.#",
    "#.#.###.#.###.#######.#.#.#.#.#.#.###.#.#.#.#",
    "#.#...#.#...#.#.....#.#...#.#.#.#...#.#...#.#",
    "#####.#.###.#.#.###.#.#####.#.#.###.#.#####.#",
    "#.....#...#.#.#...#.#.....#.#.#...#.#.....#.#",
    "#.#######.#.#.###.#######.#.#.###.#######.#.#",
    "#.#.....#.#.#...#...T...#.#.#...#.......#.#.#",
    "#.#.###.#.#.#######.###.#.#.###.#######.#.#.#",
    "#...#T..#.#.........#T..#.#...#.......#...X#",
    "#############################################",
]

HEIGHT_MAZE = len(MAZE)
LENGTH_MAZE = len(MAZE[0])

plr = {
    "messages" : [],
    "current_message":"",
    "steps_taken":0,
    "HP":100
}

def next_block(cords):
    x , y = cords
    element = MAZE[y-1][x-1]
    if element == "#":
        return 0
    elif element == "X":
        return 1
    elif element == "T":
        MAZE[y-1] = MAZE[y-1].replace("T", ".")
        return 2
    
    
def move_player(cords,next_cords):
    block = next_block(next_cords)
    plr["steps_taken"] += 1
    if block == 0:
        plr["current_message"] = "Cant walk through a barrier"
        return cords
    if block == 1:
        plr["current_message"] = "CONGRATS, YOU WON"
        plr["steps_taken"] = 0
        return (2,2)
    if block == 2:
        plr["current_message"] = "OUCH! You stepped on a trap!\n❤️ -20 HP"
        plr["HP"] -= 20
        return next_cords
    plr["current_message"] = ""
    return next_cords

def move_up(cords):
    x , y = cords
    next_cords = (x , y-1)
    return move_player(cords,next_cords)

def move_down(cords):
    x , y = cords
    next_cords = (x , y+1)
    return move_player(cords,next_cords)

def move_left(cords):
    x , y = cords
    next_cords = (x-1 , y)
    return move_player(cords,next_cords)
def move_right(cords):
    x , y = cords
    next_cords = (x+1 , y)
    return move_player(cords,next_cords)
    
def show_stats(stats_win):
    stats_win.clear()
    text = f"HP: {plr["HP"]}\nSteps Taken :{plr["steps_taken"]} \nStatus: Exploring..."
    stats_win.addstr(text)
    stats_win.refresh()

def show_maze(cords):
    PLAYER = "@"
    x , y =cords
    disp_maze = copy.deepcopy(MAZE)
    text = MAZE[y-1]
    new_txt = text[:x-1] + PLAYER + text[x:]
    disp_maze[y-1] = new_txt
    return disp_maze

def main(stdscr):
    stdscr.nodelay(True)
    maze = curses.newwin(HEIGHT_MAZE,LENGTH_MAZE+1, 1,1)
    messages = curses.newwin(3,LENGTH_MAZE+8, HEIGHT_MAZE+3,1)
    stats = curses.newwin(HEIGHT_MAZE,LENGTH_MAZE+1, 1,LENGTH_MAZE+4)

    curses.textpad.rectangle(stdscr, 0, LENGTH_MAZE+3, HEIGHT_MAZE+1 , LENGTH_MAZE*2+5)
    curses.textpad.rectangle(stdscr, HEIGHT_MAZE+2, 0, HEIGHT_MAZE+6, LENGTH_MAZE*2+5)
    curses.textpad.rectangle(stdscr, 0, 0, HEIGHT_MAZE+1, LENGTH_MAZE+2)
    
    cords = (2,2)

    while True:
        messages.clear()
        maze.clear()
        show_stats(stats)
        if plr["HP"] == 0:
            stdscr.clear()
            for char in "You lost...":
                stdscr.addstr(char)
                stdscr.refresh()
                time.sleep(0.04)
            stdscr.nodelay(False)
            stdscr.getch()
            return
        key = stdscr.getch()

        if key == curses.KEY_UP:
            cords = move_up(cords)
        elif key == curses.KEY_DOWN:
            cords = move_down(cords)
        elif key == curses.KEY_LEFT:
            cords = move_left(cords)
        elif key == curses.KEY_RIGHT:
            cords = move_right(cords)
        elif key == 27:
            return
        

        disp_maze = show_maze(cords)
        for z, line in enumerate(disp_maze):
                try:
                    maze.addstr(z, 0, line)
                except curses.error:
                    pass  # Prevents crash if it hits the bottom-right edge

        messages.addstr(plr["current_message"])
        stdscr.refresh()
        maze.refresh()
        messages.refresh()
        stdscr.move(0,0)
        time.sleep(0.05)

curses.wrapper(main)