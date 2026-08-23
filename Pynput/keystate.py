import curses
import os
import time

from pynput import keyboard

APP_RUN = True

current_state = {
    "w_pressed" : False,
    "a_pressed" : False,
    "s_pressed" : False,
    "d_pressed" : False,
}

def on_press(key):
    # print(f"Pressed : {key}")

    if getattr(key, 'char', None) in ['w','W']:
        current_state["w_pressed"] = True

    if getattr(key, 'char', None) in ['a','A']:
        current_state["a_pressed"] = True

    if getattr(key, 'char', None) in ['s','S']:
        current_state["s_pressed"] = True

    if getattr(key, 'char', None) in ['d','D']:
        current_state["d_pressed"] = True
    
    if key == keyboard.Key.esc:
        os._exit(0)

def on_release(key):
    # print(f"Released : {key}")

    if getattr(key, 'char', None) in ['w','W']:
        current_state["w_pressed"] = False

    if getattr(key, 'char', None) in ['a','A']:
        current_state["a_pressed"] = False

    if getattr(key, 'char', None) in ['s','S']:
        current_state["s_pressed"] = False

    if getattr(key, 'char', None) in ['d','D']:
        current_state["d_pressed"] = False

def print_CONTROL_PANEL():
    for key,state in current_state.items():
        if state:
            txt = "ON"
        else:
            txt = "OFF"

        print(f"{key} : {txt}")

listener = keyboard.Listener(on_press=on_press,on_release=on_release)

listener.start()
while APP_RUN:
    os.system("cls")
    print_CONTROL_PANEL()
    time.sleep(0.5)