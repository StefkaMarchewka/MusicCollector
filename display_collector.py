#display menu
from music_report import* #import file

#utworyc zmienną w mainie, która bedzie zawierac tabele (all_records)

def menu(): #pytamy co chce zrobic uzytkownik 
    while True:
        print(" 1. View full collection\n 2. Search by artist\n 3. Search by album\n 4. Search by year\n 5. Search by genre\n 6. Search by lenght\n 7. Print raport")
        answer = input("Type the number:") # trzeba aby input nie był case sensitiv, casefold?
        if answer == "1":
            draw_table(all_records)
        elif answer == "2":
            choice = input("type artist name:")
            print(search_all(all_records, choice))
        elif answer == "3":
            choice = input("type album name:")
            print(search_all(all_records, choice))
        elif answer == "4":
            choice = input("type year:")
            print(search_all(all_records, choice))
        elif answer == "5":
            choice = input("type genre name:")
            print(search_all(all_records, choice))
        elif answer == "6": #nie zrobiona
            choice = input("type lenght:") 
            print(album_time(all_records))
        elif answer == "7":
            album_sum(all_records)
            album_genre(all_records)
            print("The youngest album is: ", youngest_album(all_records))
            print("The oldest album is: ", oldest_album(all_records))
            album_time(all_records)
       
        


menu()
