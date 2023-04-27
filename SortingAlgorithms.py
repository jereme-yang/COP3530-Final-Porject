# merge sort and quick sort

def mergeSort(songList, start, end):
    if (start < end): # base case : start == end
        middle = (start + end) // 2
        mergeSort(songList, start, middle)
        mergeSort(songList, middle + 1, end)
        merge(songList, start, middle, end)

def merge(songList, start, middle, end):
    n1 = middle - start + 1
    n2 = end - middle
    x = []
    y = []

    for i in range(n1):
        x.append(songList[start+i])
    for j in range(n2):
        y.append(songList[middle+1+j])
    
    # merge x and y in order
    i = 0
    j = 0
    k = start
    while i < n1 and j < n2:
        if x[i].get_obscurity_rating() <= y[j].get_obscurity_rating():  # .getPopularity()
            songList[k] = x[i]
            i += 1
        else:
            songList[k] = y[j]
            j += 1
        k += 1
    while i < n1:
        songList[k] = x[i]
        i += 1
        k += 1
    while j < n2:
        songList[k] = y[j]
        j += 1
        k += 1


def quickSortIt(songList, low, high):

    # Stack creation
    size = high - low + 1
    stack = [0] * (size)

    # Initialization
    top = -1

    top += 1
    stack[top] = low
    top += 1
    stack[top] = high


    # While stack is not empty continue looping
    while top >= 0:
        # Pop high and low
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1

        # Partition the array and get pivot
        pivot = partition(songList, low, high)

        # Left elements - push low and pivot - 1 to stack
        if pivot - 1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = pivot - 1

        # Right elements - push high and pivot + 1 to stack
        if pivot + 1 < high:
            top += 1
            stack[top] = pivot + 1
            top += 1
            stack[top] = high

            
def partition(songList, low, high):
    pivot = songList[low].get_obscurity_rating()
    up = low
    down = high

    while up < down:
        for  j in range(low, high):
            if songList[up].get_obscurity_rating() > pivot: # getPopulatity
                break
            up += 1
        for j in range(low, high):
            if songList[down].get_obscurity_rating() < pivot: # getPopularity
                break
            down -= 1   
        if up < down:
            # swap up and down
            songList[up], songList[down] = songList[down], songList[up]
    
    # swap down with pivot
    temp = songList[low]
    songList[low] = songList[down]
    songList[down] = temp

    return down
