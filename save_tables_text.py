from pathlib import Path

a = int(input("Enter a number to start tables from: "))
b = int(input("Enter the number to which you wanna print tables: "))

FOLDER_PATH = Path("Tables Folder")

FOLDER_PATH.mkdir(parents=True,exist_ok=True)


def create_file(file_name):
    file_path = FOLDER_PATH / file_name
    with open (file_path, "w") as file:
        file.write("")
    return file_path

for i in range(a,b+1):
    file_name = f"Table of {i}"
    file_path = create_file(file_name)
    with open (file_path, "a") as file:
        str_paste = ""
        for x in range(1, 11 , 1):
            str_paste += f"{i} x {x} = {i * x}\n"
        file.write(str_paste)

print("Saved successfully")