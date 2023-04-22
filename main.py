from GenerateArtists import generate_artist_list
from SortingAlgorithms import mergeSort, quickSort
from time import sleep


artist_list = [] #holds artist objects
generate_artist_list(artist_list)

#organize data
sortingAlg = ""
while sortingAlg != '1' and sortingAlg != '2':

    sortingAlg = input("choose 1 for quicksort and 2 for mergesort : ")

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
    print("option 1: " + current_artist.get_related_artist_name_one())
    print("option 2: " + current_artist.get_related_artist_name_two())
    user_input = input("type 1 for option 1 and 2 for option 2 :")
    if (user_input == "1" or user_input == "2"): has_lost = True

