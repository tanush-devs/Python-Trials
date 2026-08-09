import sys
import time

# Color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m" # Resets text back to default

def type_writer(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

type_writer(f"{RED}CRITICAL ERROR: System corrupted!{RESET}", delay=0.04)
type_writer(f"{GREEN}Hack successful. Access granted.{RESET}", delay=0.03)