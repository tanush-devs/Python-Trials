import json

# Open the file and parse its contents
with open('01.json', 'r') as file:
    data = json.load(file)
    print(data)

# Now 'data' is a standard Python dictionary or list
with open("01.json","w") as file:
    json.dump({'monthly_budget': 0, 'expenses': []},file)
