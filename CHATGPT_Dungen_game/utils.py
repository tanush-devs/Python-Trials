import os
import time

from app_state import player_data
from UIthemes import Themes


def print_universal(TEXT, color, delay_1=0.04):
    print(color, end="", flush=True) 

    for char in TEXT:
        print(char, flush=True, end="")
        if char in ".,!":
            time.sleep(delay_1+ 0.05)
        else:
            time.sleep(delay_1)
            
    print(Themes.RESET)

def print_Danger(TEXT,delay = 0.07):
    print_universal(TEXT, color=Themes.DANGER, delay_1=delay)
    
def print_Success(TEXT, delay = 0.04):
    print_universal(TEXT, color=Themes.SUCCESS, delay_1=delay)
    
def print_Warning(TEXT, delay = 0.04):
    print_universal(TEXT, color=Themes.WARNING, delay_1=delay)
    
def print_Info(TEXT, delay = 0.04):
    print_universal(TEXT, color=Themes.INFO, delay_1=delay)

def print_Congo(TEXT, delay = 0.03):
    print_universal(TEXT, color=Themes.CONGO, delay_1=delay)
    
def game_print(TEXT, delay = 0.04):
    print_universal(TEXT, color=Themes.TEXT, delay_1=delay)

def game_print_bright_text(TEXT, delay = 0.04):
    print_universal(TEXT, color=Themes.TEXT, delay_1=delay)


def print_Death(TEXT, delay=0.02 ,word_delay = 0.14):
    print(Themes.DEATH_MESSAGE, end="", flush=True) 

    for char in TEXT:
        print(char, flush=True, end="")
        if char in ".,!":
            time.sleep(delay+ 0.025)
        elif char == " ":
            time.sleep(word_delay)
        else:
            time.sleep(delay)
            
    print(Themes.RESET)

def get_func(a:int,b:int):
    while True:
        n = input("> ")
        try:
            n = int(n)
        except ValueError:
            print_Danger("Enter a valid choice")
            continue
        
        rg = range(a,b+1)
        if n in rg:
            return n
        print_Danger("Enter a valid choice")
        continue

def update_player_data(gold_update = None, Health_update = None):
    if gold_update is not None:
        player_data["gold"] += gold_update
    
    if Health_update is not None:
        player_data["health"] += Health_update
    
def add_pause(pre_text = "",reps = 15, end="..."):
    dots = ".."
    index = 0
    for _ in range(1,reps + 1):
        pause_dots = dots[:index] + "·" + dots[index:]
        print(f"\r{pre_text}{pause_dots}",end="")
        time.sleep(0.16)
        index += 1
        if index == len(dots) + 1:
            index = 0

    print(f"\r{pre_text}{end}")
    
def clear_terminal():
    os.system("cls")