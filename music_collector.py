#music collector
from prettytable import PrettyTable


def draw_table(all_records):
    table = PrettyTable()
    table.field_names = ["artist name","album name","release year","genre","length"]
    for record in all_records: 
        table.add_row(record)
    print(table)

# blabla

def import_file1(filename):
    full_content = []
    with open(filename) as library_txt:
        data = library_txt.readlines()
        for line in data:
            new_line = line.strip().split(",")
            full_content.append(new_line)
        return full_content

all_records = import_file1("/home/stefania/Desktop/current_week/library.txt")

draw_table(all_records)

'''import_file1("/home/stefania/Desktop/current_week/library.txt")'''
