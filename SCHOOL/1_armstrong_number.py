import copy

a = int(input("Enter a number to know if its an armstrong no.: "))
b = copy.copy(a)
sum_cubes = 0
while a > 0:
    num = a%10
    sum_cubes += num**3
    a //= 10

if sum_cubes == b:
    print(f"Yes {b} is an armstrong number")
else:
    print(f"No {b} is not an armstrong number")