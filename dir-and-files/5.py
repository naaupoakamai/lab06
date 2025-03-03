output_file='/Users/azamatabilda/Desktop/1cours/2sim/PP2/lab06/dir-and-files/output.txt'
my_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
with open('output_file','w',encoding='utf-8') as file:
    for item in  my_list:
        file.write(item+'\n')
