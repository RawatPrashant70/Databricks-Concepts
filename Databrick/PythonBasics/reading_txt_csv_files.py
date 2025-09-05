import csv

path_txt = r""
with open(path_txt) as lines:
    for line in lines:
        print(line)

path_csv = r""
with open(path_csv) as lines:
    reader_object = csv.reader(lines)
    header  = next(reader_object)
    print(type(header))
    print(f"Headers : {header}")
    for rows in reader_object:
        print(rows)

    
    
