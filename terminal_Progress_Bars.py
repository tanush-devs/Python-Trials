import time

print("Downloading super top-secret files...")
for i in range(1, 101):
    bar = "█" * (i // 2) + "-" * (50 - (i // 2))
    # \r resets the cursor to the start of the line so it overwrites itself!
    print(f"\r[{bar}] {i}%", end="")
    time.sleep(0.03)

print("\nDownload complete! 🚀")








banner = r"""
  ___  _   _ _____ _   _ _____ _   _ 
 / _ \| | | |_   _| | | |  ___| \ | |
/ /_\ \ | | | | | | |_| | |__ |  \| |
|  _  | | | | | | |  _  |  __| | . ` |
| | | | |_| | | | | | | | |___| |\  |
\_| |_/\___/  \_/ \_| |_/\____/\_| \_/
"""
print(banner)

