import random

def partition3(arr, low, high):
    """
    fucntion: function that imlements the 3 partition technique
    input: list of integers, start and end index
    return value: tuple of 2 integers, 1st int denotes end of 1st partition, 2nd int denotes start of 2nd partition
    """
    pivot = arr[low]
    i = low+1
    # if value is less than pivot then put it in the 1st partition
    # if value is greater than pivot then put it in the 2nd partition 
    # otherwise keep it in the middle
    while i <= high: 
        if arr[i] < pivot: 
            arr[i], arr[low] = arr[low], arr[i]
            i += 1
            low += 1
        elif arr[i] > pivot:
            arr[high], arr[i] = arr[i], arr[high]
            high -= 1
        else:
            i += 1
    return (low, high)


def q3_sort(arr, low, high):
    """
    Function: function that implements the 3 partition quick sort for a list of integers
    input: an list of integer value
    return value: a list of sorted integer values
    """
    while low < high:
        index = random.randint(low, high) # choose a random pivot in the array
        arr[low], arr[index] = arr[index], arr[low] 
        m1, m2 = partition3(arr,low,high) # m1 = end point of 1st partition and m2 = start of 2nd partition
        if (m1-low) < (high-m2): # if 1st partition is smaller then recursively sort it first, solve 2nd partition otherwise
            q3_sort(arr, low, m1-1)
            low = m2+1
        else: 
            q3_sort(arr, m2+1, high)
            high = m1-1
    return arr

def main():
    """
    function: Driver code that handles input and calls the sorting procedure
    input: None
    return: None
    """
    arr = list(map(int, input().split()))
    arr = q3_sort(arr, 0, len(arr)-1)
    for i in arr:
        print(i, end=" ")
    print()
    
    
if __name__ == "__main__":
    main()
