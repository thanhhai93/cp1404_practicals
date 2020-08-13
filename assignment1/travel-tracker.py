"""
Replace the contents of this module docstring with your own details
Name: NGUYEN THANH HAI
Date started: 30/7/2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-1-travel-tracker-thanhhai93/blob/master/assignment1.py
"""

''''Here are the global lists which will be used in the function, also the command to open the songs.csv file. I 
import csv library just in case i have to use some of its function to interact with the csv file. one important list 
to notice is the FILE_LIST in which will store all valuable data from main_menu(), list_function, add_function() and 
learnt_function() '''
import csv

def main():
    print("Travel Tracker 1.0 - by <NGUYEN THANH HAI>")
    main_menu()


def list_function():
    count = 0
    count_learnt = 0

    list = []
    for lines in FILE_LIST:
        count += 1
        new_lines = lines.split(',')
        input_place = new_lines[0]
        input_country = new_lines[1]
        input_priority = new_lines[2]
        learn = new_lines[3].replace("l", "*").replace("u", "").replace("\n", "")
        list.append(count)
        songs_display = ("{:>2}. {:<1} {:<35} - {:<35} ({})".format(count, learn, input_place, input_country, input_priority))
        print(place_display)

        if "*" in learn:
            count_learnt += 1
        print("-" * 100)
        print("Total place loaded: ", max(list))
        count_need = (max(list) - count_learnt)
        REMAINDER.append(count_need)
        print(max(list) - count_learnt, "place still to learn")
        print(count_learnt, "place learned")
        TOTAL_PLACE.append(max(list))
        print("-" * 100)
        main_menu()



def main_menu():
    print("Menu:")
    count_load = 0
    for lines in FILE_LIST:
        count_load += 1
    print(count_load, )

    print("L - List places")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")
    menu = input(">>>").upper()
    while menu not in ["L", "A", "M", "Q"]:
        menu = input ("Invalid, please re-enter and appropriate option: ").upper()
    if menu == "L":
        list_function()
    if menu == "A":
        add_function()
    if menu == "C":
        learnt_function()
    else:
        confirm = input("Are you sure you want to quit? -(Y)es, (N)o ").upper()
        while confirm not in ["Y", "N"]:
            confirm = input("Invalid, please re-enter your option: (Y)es or (N)o").upper()
        if confirm == "Y":
            with open("place.csv", "w") as place_list:
                for item in FILE_LIST:
                    place_list.write("{}".format(item))
                print("---Saving to your csv file---")
                print("-- Exited playlist. Have a nice day! --")
                quit()
        else:
            main_menu()







if __name__ == '__main__':
    main()

