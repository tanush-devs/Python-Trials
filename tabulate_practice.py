from tabulate import tabulate


# Data structured as a list of lists
data={"monthly_budget": 100000, "categories": ["food", "cources"], "expenses": [{"amount": 2000.0, "category": "food", "note": "Pizza"}, {"amount": 200.0, "category": "food", "note": "burger"}, {"amount": 50000.0, "category": "cources", "note": "coding"}]}

# Define your columns
headers = ["Amount", "Category", "Note"]
Temp=[]
table_list=[]
# Print the basic table
for i in range (0,len(data["expenses"])):

    Temp.append(data["expenses"][i]["amount"])
    Temp.append(data["expenses"][i]["category"])
    Temp.append(data["expenses"][i]["note"])

    table_list.append(Temp)


print(table_list)
print(tabulate(table_list,headers=headers))