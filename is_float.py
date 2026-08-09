def is_float(a):
    try:
        float(a)
        return True
    except Exception:
        return False
    
while True:
    a= input("> ")
    if is_float(a):
        print("True")
    else:
        print("False")