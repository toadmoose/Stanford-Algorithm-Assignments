def get_pivot(arr, low, high):
    mid = (low + high) // 2
    s = sorted([(arr[low], low), (arr[mid], mid), (arr[high], high)])
    return s[1][1]

def partition(arr, low, high):
    pivot_index = get_pivot(arr, low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        left_count = quicksort(arr, low, pi - 1)
        right_count = quicksort(arr, pi + 1, high)
        return left_count + right_count + (high - low)
    return 0

def count_quicksort_comparisons(filename):
    with open(filename, 'r') as file:
        arr = [int(line.strip()) for line in file]
    return quicksort(arr, 0, len(arr) - 1)

# Assuming the file is named 'QuickSort.txt' and is in the same directory
filename = 'QuickSort.txt'
total_comparisons = count_quicksort_comparisons(filename)

print(f"Total number of comparisons: {total_comparisons}")
