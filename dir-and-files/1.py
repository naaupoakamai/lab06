import os
from pathlib import Path

def list_directories(link):
    directories=[]
    for i in Path(link).iterdir():
        if i.is_dir():
            directories.append(i.name)
    return directories

def list_file(link):
    files=[]
    for j in Path(link).iterdir():
        if j.is_file():
            files.append(j.name)
    return files

def list_all(link):
    all=[]
    for ji in Path(link).iterdir():
        all.append(ji.name)
    return all

path=input('link?').strip()
if not os.path.exists(path):
    print("The specified path does not exist. Please enter a valid path.")

print("\nChoose what exactly you want to display:")
print("1. Only directories (folders)")
print("2. Only files")
print("3. All directories and files")

choice = input("\nEnter the option number (1, 2 or 3): ").strip()
if choice == '1':
    directories = list_directories(path)
    print("\nList of directories in the specified path:")
    if directories:
        for directory in directories:
            print(directory)
    else:
        print("No directories found.")
elif choice == '2':
    files = list_file(path)
    print("\nList of files in the specified path:")
    if files:
        for file in files:
            print(file)
    else:
        print("Files not found.")
elif choice == '3':
    contents = list_all(path)
    print("\nList of all directories and files in the specified path:")
    if contents:
        for item in contents:
            print(item)
    else:
        print("Contents not found. Directory is empty.")
else:
    print("\nError: Invalid option entered. Please enter 1, 2 or 3.")