#music reports
from prettytable import PrettyTable
from collections import Counter
import sys
import os


def import_file(filename):
    full_content = []
    with open(filename) as library_txt:
        data = library_txt.readlines()
        for line in data:
            new_line = line.strip().split(",")
            full_content.append(new_line)
        return full_content


all_records = import_file("library.txt")  #cały kontent'''
                           #cała scieżka dostepu musi byc


def draw_table(all_records):  #działa!
    table = PrettyTable()
    table.field_names = ["Artist name","Album name","Release year","Genre","Length"]
    for record in all_records: 
        table.add_row(record)
    return table

# printed_table = draw_table  '''to był potrzebne przy importowaniu zmiennych


def search_all(all_records, answer): #dziala, wyszukuje wszystkie rekordy dla danego klucza
    search_key = []
    for record in all_records:
        if answer in record:
            search_key.append(record)
    return draw_table(search_key) #trzeba zmienić printy na returny
                      

def youngest_album(all_records): #działa!!! 
    years = []
    for record in all_records:
        years.append(int(record[2])) #żeby wybrac min i max elementy listy musza byc int
    youngest = max(years)
    for record in all_records:  #iterowac można po iteratorach! nie moze iterowac po wybranych elementach listy, moze po całych listach
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
        

def shortest_album(all_records): #działa!
    times = []  #zrobic jeden słownik a nie dwie listy
    duration = []
    for record in all_records:
        times.append(record[4])
    for item in times:
        (m, s) = item.split(":")
        result = int(m) * 60 + int(s)
        duration.append(result)
        shortest = min(duration)
        short_ind = (duration.index(shortest))  #indeks na liscie najkrótszego albumu
    min_minutes = times[short_ind]
    for record in all_records:  
        if min_minutes == record[4]: 
           return record


def longest_album(all_records): #działa!
    times = []  #zrobic jeden słownik a nie dwie listy
    duration = []
    for record in all_records:
        times.append(record[4])
    for item in times:
        (m, s) = item.split(":")
        result = int(m) * 60 + int(s)
        duration.append(result)
        longest = max(duration)
        long_ind = (duration.index(longest)) #indeks na liscie najdłuższego albumu
    max_minutes = times[long_ind] #pokazuje najdłuzszy czas
    for record in all_records:  
        if max_minutes == record[4]: 
            return record
        

def album_sum(all_records):
    return len(all_records)


def album_genre(all_records):
    genres = []
    for record in all_records:
        genres.append(record[3])
    return Counter(genres)

def time_range(all_records):
    input_range = []
    first_year = int(input("choose start year:"))
    second_year = int(input("choose end year:"))
    input_range.append(first_year)
    input_range.append(second_year)
    result = []
    for record in all_records:
        if int(record[2]) in range(input_range[0], input_range[1]+1):
            result.append(record)
    return draw_table(result)






