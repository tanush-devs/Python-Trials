import time
import os
from colorama import Fore,init

init(autoreset=True)

def stop_watch():
    start = time.time()
    seconds = 0
    minutes = 0
    hours = 0
    while True:
        
        elapsed = int(time.time() - start)

        # seconds = elapsed % 60
        # minutes = (elapsed // 60) % 60
        # hours = elapsed // 3600
        
        hours, remainder = divmod(elapsed, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        time.sleep(1)
        
        os.system("cls")
        StopWatch = f"{hours:02}:{minutes:02}:{seconds:02}"
        print(StopWatch)


def timer(target_time = 0):
    start = time.time()
    
    target_hours, remainder = divmod(target_time, 3600)
    target_minutes, target_seconds = divmod(remainder, 60)
    
    while True:
        
        elapsed = int(time.time() - start)
        hours, remainder = divmod(elapsed, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        time.sleep(1)
        
        StopWatch = f"{hours:02}:{minutes:02}:{seconds:02}"
        
        os.system("cls")
        if hours == target_hours and minutes == target_minutes and seconds == target_seconds:
            print(StopWatch)
            print(Fore.GREEN + "Target time reached")
            return
        
        print(StopWatch)



timer(1)