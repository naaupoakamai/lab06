def are_all_elements_true(t):
    return all(t)

t1 = (1, "Hello", True, 3.14)
print("Все элементы кортежа t1 истинны?", are_all_elements_true(t1))
t2 = (1, 0, "Hello")
print("Все элементы кортежа t2 истинны?", are_all_elements_true(t2))