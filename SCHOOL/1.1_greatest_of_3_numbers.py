def get_int():
    try:
        a = float(input("Enter a number: "))
    except ValueError:
        print("Choose a valid number")
    except Exception:  # noqa: BLE001
        return
    return a

a = get_int()
b = get_int()
c = get_int()

print(f"The greatest number is: {max([a,b,c])}")