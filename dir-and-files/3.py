import os
path=input("link?").strip()  
if os.path.exists(path):
    print("Path exists.")
    if os.path.isfile(path):
        print("This is a file.")
        file_name = os.path.basename(path)
        parent_directory = os.path.dirname(path)
        print(f"File Name: {file_name}")
        print(f"Parent Directory: {parent_directory}")

    elif os.path.isdir(path):
        print("This is a directory.")
        parent_directory = os.path.dirname(path)
        print(f"Parent Directory: {parent_directory}")
else:
    print("Path does not exist.")