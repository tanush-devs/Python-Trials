import random

import helpers
import monsters
import utils
from UIthemes import Themes


def room_monster():
    a = random.randint(1,1)
    if a == 1:
        monsters.monster_Wolf()

def room_trasure():
    chest = helpers.random_chest()
    
    utils.print_Info(f"You found a {chest}")
    utils.game_print("1. Open it")
    utils.game_print("2. Leave it")
    confirmation = utils.get_func(1,2)
    if confirmation == 1:
        utils.add_pause("Opening chest")
        if chest == "wooden chest":
            helpers.wooden_chest()
        elif chest == "golden chest":
            helpers.golden_chest()
    elif confirmation == 2:
        utils.game_print_bright_text("Successfully skipped...")
        utils.game_print_bright_text("Press Enter to return to the next room")
        input("> ")
        

def room_potion():
    utils.print_Info("You discover a glowing potion.")
    utils.game_print("1. Drink it")
    utils.game_print("2. Leave it")
    confirmation = utils.get_func(1,2)
    if confirmation == 1:
        helpers.drink_potion()
    elif confirmation == 2:
        utils.game_print_bright_text("Successfully skipped...")
        utils.game_print_bright_text("Press Enter to return to the next room")
        input("> ")
    

def room_trap():
    print(Themes.WARNING)
    utils.add_pause("You step into the next room")
    print(Themes.RESET)
    a = random.randint(1,3)
    if a == 1:
        helpers.spike_trap()
    elif a == 2:
        helpers.bounder_trap()
    elif a == 3:
        helpers.fire_trap()

def room_empty():
    a = random.randint(1,2)
    if a == 1:
        helpers.silent_room()
    elif a ==2:
        helpers.campfire_room()
