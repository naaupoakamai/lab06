from os import *

link=input('Path?')
if path.exists(link):
    print("There is a way.")
    if access(link, R_OK):
        print("Readable.")
    else:
        print("Insufficient permissions to readable.")

    if access(link, W_OK):
        print("Writable.")
    else:
        print("Insufficient permissions to write.")

    if access(link, X_OK):
        print("Executable.")
    else:
        print("Not executable.")
else:
    print("There is not a way")
