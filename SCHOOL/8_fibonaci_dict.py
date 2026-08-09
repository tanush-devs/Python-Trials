import os

fibonaci_temp = {"First":0 , "Second":1 , "Sum":1}


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def confirmation():
    while True:
        confirmation = input("(Y/N): ").strip().lower()
        if confirmation == "yes" or confirmation == "y":
            return True
        elif confirmation == "no" or confirmation == "n" or confirmation == "noo":
            return False
        else:
            print("Enter (yes/no)")
            
def update_fibonaci_dict():
    fb = fibonaci_temp
    
    fb["First"] = fb["Second"]
    fb["Second"] = fb["Sum"]
    fb["Sum"] = fb["First"] + fb["Second"]

current_runs = 0
MAX_RUNS = 10

clear_terminal()
print(f"{fibonaci_temp["First"]}\n{fibonaci_temp["Second"]}")
while True:
    print(fibonaci_temp["Sum"])
    update_fibonaci_dict()
