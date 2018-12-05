#music reports
from prettytable import PrettyTable
from collections import Counter


def import_file(filename):
    full_content = []
    with open(filename) as library_txt:
        data = library_txt.readlines()
        for line in data:
            new_line = line.strip().split(",")
            full_content.append(new_line)
        return full_content

all_records = import_file("/home/stefania/Desktop/current_week/library.txt")  #cały kontent'''
                           #cała scieżka dostepu musi byc

def draw_table(all_records):  #działa!
    table = PrettyTable()
    table.field_names = ["artist name","album name","release year","genre","length"]
    for record in all_records: 
        table.add_row(record)
    print(table)

printed_table = draw_table

# def search_by_sth(all_records, answer):  #zwraca tylko pieprwszy znaleziony rekord
#     for record in all_records:
#         if answer in record:
#             return record

def search_all(all_records, answer): #dziala, wyszukuje wszystkie rekordy dla danego klucza
    search_key = []
    for record in all_records:
        if answer in record:
            search_key.append(record)
    return search_key #trzeba zmienić printy na returny
                      

def youngest_album(all_records): #działa!!! 
    years = []
    for record in all_records:
        years.append(int(record[2])) #żeby wybrac min i max elementy listy musza byc int
    youngest = max(years)
    for record in all_records:  #iterowac można po itertorach! nie moze iterowac po wybranych elementach listy, moze po całych listach
        if youngest == int(record[2]): 
            return record
 
 
def oldest_album(all_records): 
    years = []
    for record in all_records:
        years.append(int(record[2])) #żeby wybrac min i max elementy listy musza byc int
    oldest = min(years)
    for record in all_records:  #iterowac można po itertorach! nie moze iterowac po wybranych elementach listy, moze po całych listach
        if oldest == int(record[2]): 
            return record  
        

def album_time(all_records): #działa!
    times = []  #zrobic jeden słownik a nie dwie listy
    duration = []
    for record in all_records:
        times.append(record[4])
    for item in times:
        (m, s) = item.split(":")
        result = int(m) * 60 + int(s)
        duration.append(result)
        longest = max(duration)
        shortest = min(duration)
        long_ind = (duration.index(longest)) #indeks na liscie najdłuższego albumu
        short_ind = (duration.index(shortest))  #indeks na liscie najkrótszego albumu
    max_minutes = times[long_ind] #pokazuje najdłuzszy czas
    min_minutes = times[short_ind]
    for record in all_records:  
        if max_minutes == record[4]: 
            print("the longest album:", record)
        if min_minutes == record[4]: 
            print("the shortest album:", record)


def album_sum(all_records):
    print("Collection contains ", len(all_records), "albums")

def album_genre(all_records):
    genres = []
    for record in all_records:
        genres.append(record[3])
    print(Counter(genres))



