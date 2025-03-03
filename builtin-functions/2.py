import re

def count_latter(list):
    upper_count=re.findall(r'[A-Z]',list)
    lower_count=re.findall(r'[a-z]',list)
    return len(upper_count),len(lower_count)

user_input = input("Введите строку: ")
upper, lower = count_latter(user_input)
print("Количество букв верхнего регистра:", upper)
print("Количество букв нижнего регистра:", lower)