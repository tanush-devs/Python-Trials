def factorail(num):
    if num == 1 or num == 0:
        return 1

    return num * factorail (num - 1)

def find_summation(x, total_terms):
    summation = 0
    for i in range(total_terms,0, -1):
        if i == 1:
            return summation + x
        elif i % 2 == 0:
            summation += (x**i)/factorail(i)
        elif i % 2 != 0:
            summation += -(x**i)/factorail(i)

x = int(input("Choose a value for X: "))
n = int(input("Till what range do you wanna find the summation: "))

answer = find_summation(x, n)

print(f"Summision of {n} terms of the sequence is {answer}")


## without functions/school level

summation = 0
for i in range(1,n+1):
    if i == 1:
        summation += x
    elif i%2 == 0:
        summation += (x**i)/factorail(i)
    elif i%2 != 0:
        summation += -(x**i)/factorail(i)
    else:
        pass
    
print(f"Summation of {n} terms of the sequence is {summation}")