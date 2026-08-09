import os

print("This is a fibonaci series starting from 0")

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

def generate_next_fibonaci_number(a,b):
    return(a + b)

def get_updated_numbers(a,b):
    c = generate_next_fibonaci_number(a,b)
    return(b,c)


current_runs = 0
MAX_RUNS = 10

clear_terminal()
num_1 = 0
num_2 = 1
print(f"{num_1}\n{num_2}")
while True:
    print(generate_next_fibonaci_number(num_1,num_2))
    num_1,num_2 = get_updated_numbers(num_1,num_2)

    if current_runs > MAX_RUNS:
        print("Do you want to continue generating fibonaci series?")
        if not confirmation():
            clear_terminal()
            break
        
        current_runs = 0
        continue
    
    current_runs += 1
