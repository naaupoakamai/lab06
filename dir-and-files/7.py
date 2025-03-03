source_file = "/Users/azamatabilda/Desktop/1cours/2sim/PP2/lab05/row.txt"
destination_file = "/Users/azamatabilda/Desktop/1cours/2sim/PP2/lab06/dir-and-files/output.txt"

with open(source_file, "r", encoding="utf-8") as src:
        content = src.read()

with open(destination_file, "w", encoding="utf-8") as dest:
        dest.write(content)
