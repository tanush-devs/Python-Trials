import random

import utils


class monster:
    def __init__(self,name,health,attack_range,Reward_range):
        self.name = name
        self.health = health
        self.attack_range = attack_range
        self.Reward_range = Reward_range
    
    def attack(self):
        atk = self.attack_range
        damage = random.randint(atk[0],atk[1])
        utils.update_player_data(Health_update=-damage)
        utils.print_Danger(f"{self.name} dealt you a damage of {damage}")

def monster_Wolf():
    wolf = monster("Wolf",12,[2,5],[12,20])
    utils.print_Warning("A wild wolf attacks!")
    
    utils.print_Info("Wolf HP: 12\nWolf attack: 2-5\nReward: 12-20 gold")
    wolf.attack()
