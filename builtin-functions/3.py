def polindrom(str):
    str=str.lower()
    str1=str[::-1]
    if str==str1:
        return True
    else:return False

str=input()
print(polindrom(str))