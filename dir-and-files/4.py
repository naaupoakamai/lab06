input_file='/Users/azamatabilda/Desktop/PP2/lab05/row.txt'
with open(input_file,'r',encoding='utf-8') as file:
    line_count=sum(1 for i in file)
print(f"Count:{line_count}")