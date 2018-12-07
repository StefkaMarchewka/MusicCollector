#display menu
from music_report import* #import file


def menu(): #pytamy co chce zrobic uzytkownik 
    os.system("clear")
    user_not_pressed_defined_number = True
    while user_not_pressed_defined_number:
        
        print(""" 
        MENU    
    1. View full collection
    2. Search by artist 
    3. Search by album 
    4. Search by year 
    5. Search by genre
    6. Search by lenght 
    7. Print report
    8. Exit
    """)
        answer = input("Choose the option from menu (number):") 
        if answer == "1":
            os.system("clear")
            print(draw_table(all_records))
        elif answer == "2":
            os.system("clear")
            choice = input("Type artist name:")
            print(search_all(all_records, choice))
        elif answer == "3":
            os.system("clear")
            choice = input("Type album name:")
            print(search_all(all_records, choice))
        elif answer == "4":
            os.system("clear")
            print(time_range(all_records))
        elif answer == "5":
            os.system("clear")
            choice = input("Type genre name:")
            print(search_all(all_records, choice))
        elif answer == "6": 
            os.system("clear")
            choice = input("choose longest(L) or shortest(S) album:") 
            if choice == "L":
                print("The longest album is:", longest_album(all_records))
            elif choice == "S":
                print("The shortest album is:", shortest_album(all_records))
        elif answer == "7":
            os.system("clear")
            print("Collection report:")
            print("Collection contains ", album_sum(all_records), "albums")
            print("Albums by genre:", album_genre(all_records))
            print("The youngest album is: ", youngest_album(all_records))
            print("The oldest album is: ", oldest_album(all_records))
            print("The shortest album is:", shortest_album(all_records))
            print("The longest album is:", longest_album(all_records))
        elif answer == "8":
            user_not_pressed_defined_number = False
        elif not answer.isnumeric(): 
            os.system("clear")
            print("Wrong input, choose a number")
       
        


menu()
