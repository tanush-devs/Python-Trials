def factorail(num):
    if num == 1 or num == 0:
        return 1
    
    return num * factorail (num - 1)

def next_occurence(x,occurence_num):
    if occurence_num == 1:
        return x
    else:
        if occurence_num % 2 == 0:
            return (x**occurence_num) / factorail(occurence_num)
        elif occurence_num % 2 != 0:
            return -((x**occurence_num) / factorail(occurence_num))

x = int(input("Choose a value for X: "))
n = int(input("Till what range do you wanna find the summision: "))

answer = 1
for i in range(1,n+1):
    answer *= next_occurence(x, i)

print(f"Summision of {n} terms of the sequence is {answer}")
