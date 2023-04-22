from GenerateArtists import generate_artist_list
from SortingAlgorithms import mergeSort, quickSort
from time import sleep
from random import randint


artist_list = [] #holds artist objects
generate_artist_list(artist_list)

#organize data
sortingAlg = ""
while sortingAlg != '1' and sortingAlg != '2':

    sortingAlg = input("choose 1 for quicksort and 2 for mergesort: ")

    match sortingAlg:
        case "1":
            quickSort(artist_list, 0, len(artist_list)-1)
        case "2": 
            mergeSort(artist_list, 0, len(artist_list)-1)

#begin game mechanics
score = 0
level = 0
has_lost = False
current_index = len(artist_list)-1
while (not has_lost):
    current_artist = artist_list[current_index]
    print(f'LEVEL : {level}\n NAME OF ARTIST : {current_artist.get_name()}\n')
    options = [current_artist.get_related_artist_name_one(), current_artist.get_related_artist_name_two()]
    random_index = randint(0, 1)
    correct_option = "1" if random_index == 0 else "2"
    if (correct_option == "1"):
        print("Option 1: "+ options[0])
        print("Option 2: "+ options[1])
    else:
        print("Option 1: "+ options[1])
        print("Option 2: "+ options[0])
    user_input = input("type 1 for option 1 and 2 for option 2: ")
    if (user_input == correct_option):
        score += 1
        level += 1
        current_index -= 1
    else:
        has_lost = True
        print("you lost! Your final score: " + str(score))


