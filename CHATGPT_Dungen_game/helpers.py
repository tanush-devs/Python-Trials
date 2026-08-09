import random
import time

import app_state
import utils
from UIthemes import Themes


def random_chest():
    a = random.randint(1,2)
    if a == 1:
        return "wooden chest"

    elif a == 2:
        return "golden chest"
    
def wooden_chest():
    a = random.randint(1,3)
    if a == 1:
        gold = random.randint(2,8)
        reward_gold(gold)

    elif a == 2:
        gold = random.randint(2,10)
        diamond = 1
        reward_diamond(gold,diamond)

    elif a == 3:
        gold = random.randint(2,4)
        health_deduction = random.randint(6,10)
        reward_trap(gold,health_deduction)

def golden_chest():
    a = random.randint(1,6)
    
    if a == 1 or a == 2 or a == 3:
        gold= random.randint(4,12)
        reward_gold(gold)
        
    elif a == 4 or a == 5:
        gold= random.randint(4,12)
        diamond = random.randint(1,3)
        reward_diamond(gold,diamond)

    elif a == 6:
        gold= random.randint(2,6)
        health_deduction = random.randint(4,7)
        reward_trap(gold,health_deduction)

def reward_gold(gold):
    utils.update_player_data(gold_update=gold)
    utils.print_Congo(f"Congratulations! You got {gold} gold from the chest")

def reward_diamond(gold,diamond):
    utils.update_player_data(gold_update=gold+(diamond*5))
    utils.print_Congo(f"Congratulations! You got {gold} gold from the chest")
    utils.print_Warning("Wait.....")
    utils.print_Success(f"💎 You found {diamond} mysterious gem!")
    utils.print_Congo(f"Congratulations! You got {diamond*5} extra gold for the diamonds")

def reward_trap(gold,health_deduction):
    utils.update_player_data(gold_update=gold , Health_update= -health_deduction)
    utils.print_Congo(f"Congratulations! You got {gold} gold from the chest")
    utils.print_Warning("Wait.....")
    utils.print_Danger("It was a trapped chest")
    utils.print_Danger(f"You lost {health_deduction} health")
 
def drink_potion():
    a = random.randint(1,3)
    if a == 2 or a == 3:
        print(Themes.WARNING)
        utils.add_pause("🧪 You drank the potion")
        print(Themes.RESET)
        health_recovery = random.randint(4,8)
        utils.update_player_data(Health_update= +health_recovery)
        utils.print_Success("🧪 Healing Potion!")
        utils.print_Congo(f"❤️ +{health_recovery} HP")

    elif a == 1:
        print(Themes.WARNING)
        utils.add_pause("🧪 You drank the potion")
        print(Themes.RESET)
        health_deduction = random.randint(3,6)
        utils.update_player_data(Health_update= -health_deduction)
        utils.print_Danger("🤢 Uh oh.")
        utils.print_Danger("It's poisonous!")
        utils.print_Danger(f"❤️ -{health_deduction} HP")


def spike_trap():
    utils.update_player_data(Health_update= -5)
    utils.print_Danger("CLICK.", delay= 0.1)
    utils.print_Danger("🗡️ SPIKE TRAP!")
    utils.print_Danger("❤️ -5 HP")
    input("> ")
    
def bounder_trap():
    utils.print_Danger("A giant boulder starts rolling toward you!", delay= 0.1)
    utils.game_print("🎲 Press enter to roll for your escape...")
    input("> ")
    speed = random.randint(1,6)
    utils.game_print(f"You rolled: {speed}")
    rolling_boulder(speed)
    input("> ")

def fire_trap():
    utils.print_Danger("🔥 The floor catches fire!!", delay= 0.1)
    utils.update_player_data(Health_update= -2)
    utils.print_Danger("❤️ -2 HP")
    input("> ")

def rolling_boulder(speed_man, speed_boulder = 3.4):
    SUB_POSITIONS = 2.5
    if speed_man == 1:
        speed_boulder = 1.8
    elif speed_man == 2:
        speed_boulder = 2.6
    elif speed_man == 5:
        speed_boulder = 3.6
        SUB_POSITIONS = 4
    elif speed_man == 6:
        speed_boulder = 4.8
        SUB_POSITIONS = 4
    cords_man = 30
    cords_boulder = 0
    plane = f"🚪{"·"*60}"
    while True:
        index_man = int(len(plane) - cords_man//SUB_POSITIONS)
        index_boulder = int(len(plane) - cords_boulder//SUB_POSITIONS)
        
        current_frame = plane[:index_man] + "🏃" + plane[index_man:index_boulder] + "🌑" +plane[index_boulder:]
        
        if index_man >= index_boulder:
            current_frame = plane[:index_man] + "💥😵💥" + plane[index_man:]
            
            print(f"\r{current_frame}",end="\n\n")
            utils.print_Death("You died, the boulder hit you")
            app_state.is_alive = False
            return
        elif index_man <= 0:
            current_frame = "🕺" + plane[:index_boulder] + "💥" +plane[index_boulder:]
            
            print(f"\r{current_frame}",end="\n\n")
            utils.print_Congo("웃 You escaped!")
            return

        else:
            print(f"\r{current_frame}",end="")
            cords_man += speed_man
            cords_boulder += speed_boulder
            time.sleep(0.05)
            

def campfire_room():
    utils.print_Info("The room is completely silent...")
    time.sleep(1)
    utils.print_Info("You find a small campfire.")
    time.sleep(1)
    print(Themes.INFO)
    utils.add_pause("🔥 You rest", reps=40)
    print(Themes.RESET)
    utils.update_player_data(Health_update=+2)
    utils.print_Congo("❤️ +2 HP")

def silent_room():
    utils.print_Info("The room is completely silent...")
    time.sleep(0.3)
    utils.print_Info("Nothing happens.")
    time.sleep(1)
    print(flush=True)
    utils.print_Info("You enjoy the suspicious silence 💀")
    print(Themes.NARRATION)
    utils.add_pause("You return to the main room", reps=30)
    print(Themes.RESET)

