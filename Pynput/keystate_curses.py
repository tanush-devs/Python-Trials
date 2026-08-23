import curses
import os
import time

from pynput import keyboard

APP_RUN = True

current_state = {
    "W" : False,
    "A" : False,
    "S" : False,
    "D" : False,
}

def on_press(key):
    # print(f"Pressed : {key}")

    if getattr(key, 'char', None) in ['w','W']:
        current_state["W"] = True

    if getattr(key, 'char', None) in ['a','A']:
        current_state["A"] = True

    if getattr(key, 'char', None) in ['s','S']:
        current_state["S"] = True

    if getattr(key, 'char', None) in ['d','D']:
        current_state["D"] = True
    
    if key == keyboard.Key.esc:
        os._exit(0)

def on_release(key):
    # print(f"Released : {key}")

    if getattr(key, 'char', None) in ['w','W']:
        current_state["W"] = False

    if getattr(key, 'char', None) in ['a','A']:
        current_state["A"] = False

    if getattr(key, 'char', None) in ['s','S']:
        current_state["S"] = False

    if getattr(key, 'char', None) in ['d','D']:
        current_state["D"] = False

def print_CONTROL_PANEL(stdscr):
    stdscr.erase()
    index = 1
    for key,state in current_state.items():
        if state:
            txt = "ON"
        else:
            txt = "OFF"

        text = f"{key} : {txt}"
        stdscr.addstr(index,1,text)
        stdscr.refresh()
        index += 1


def main(stdscr):
    listener = keyboard.Listener(on_press=on_press,on_release=on_release)
    listener.start()

    while True:
        print_CONTROL_PANEL(stdscr)
        time.sleep(0.1)
    
curses.wrapper(main)