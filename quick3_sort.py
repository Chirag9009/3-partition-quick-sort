import random

def partition3(arr, low, high):
    pivot = arr[low]
    i = low+1
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
    while low < high:
        index = random.randint(low, high)
        arr[low], arr[index] = arr[index], arr[low]
        m1, m2 = partition3(arr,low,high)
        if (m1-low) < (high-m2):
            q3_sort(arr, low, m1-1)
            low = m2+1
        else:
            q3_sort(arr, m2+1, high)
            high = m1-1
    return arr


n = int(input())
arr = list(map(int, input().split()))
arr = q3_sort(arr, 0, len(arr)-1)
for i in arr:
    print(i, end=" ")
print()