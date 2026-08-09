pos_count = 0
def check_int(a):
    try:
        int(a)
        return True
    except ValueError:
        return False
while True:
    a = input("Enter a number [S] - stop: ")
    if check_int(a):
        if int(a) > 0:
            pos_count += 1
    else:
        if a.strip().lower() in ["s","stop"]:
            break
        else:
            print("Choose correctly")

print(f"Total count of positive numbers entered were :  {pos_count}")