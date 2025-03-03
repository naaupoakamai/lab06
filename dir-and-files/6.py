from string import ascii_uppercase
letters=ascii_uppercase
for letter in letters:
    file_name=f'{letter}.txt'
    with open(file_name,'w',encoding='utf-8') as file:
        file.write(f'Этот файл называется {file_name}')
    print(f"Файл {file_name} создан успешно.")