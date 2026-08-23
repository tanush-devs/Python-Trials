import os
import time

frame = 0
TARGET_FPS = 30
FRAME_BUDGET = 1 / TARGET_FPS

st_main = time.perf_counter()

while True:
    start_time = time.perf_counter()

    os.system("cls")
    print(frame)
    frame += 1

    if frame == 60:
        break

    end_time = time.perf_counter()
    total_time = end_time - start_time
    delay_needed = FRAME_BUDGET - total_time

    if delay_needed > 0:
        time.sleep(delay_needed)

end_main = time.perf_counter()

Actual_fps = frame / (end_main - st_main)
print(f"Actual fps: {Actual_fps:.2f}")