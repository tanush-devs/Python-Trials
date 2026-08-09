import helpers
import utils

utils.clear_terminal()
while True:
    a = int(input("(1/2): "))
    if a == 1:
        print("wooden chest")
        helpers.wooden_chest()
        helpers.wooden_chest()
    elif a ==2:
        break
utils.clear_terminal()
while True:
    a = int(input("(1/2): "))
    if a == 1:
        print("golden chest")
        helpers.golden_chest()
        helpers.golden_chest()
    elif a ==2:
        break

utils.clear_terminal()
while True:
    a = int(input("(1/2): "))
    if a == 1:
        print("Spike trap")
        helpers.spike_trap()
    elif a ==2:
        break

utils.clear_terminal()
while True:
    a = int(input("(1/2): "))
    if a == 1:
        print("Boulder trap")
        helpers.bounder_trap()
    elif a ==2:
        break

utils.clear_terminal()
while True:
    a = int(input("(1/2): "))
    if a == 1:
        print("Fire trap")
        helpers.fire_trap()
    elif a ==2:
        break

utils.clear_terminal()
while True:
    a = int(input("(1/2): "))
    if a == 1:
        print("Campfireroom")
        helpers.campfire_room()
    elif a ==2:
        break

utils.clear_terminal()
while True:
    a = int(input("(1/2): "))
    if a == 1:
        print("Silent room")
        helpers.silent_room()
    elif a ==2:
        break
