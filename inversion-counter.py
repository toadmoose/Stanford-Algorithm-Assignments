def merge_and_count(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len, right_len = len(left), len(right)
    
    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i  # Count inversions
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result, count

def sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, left_count = sort_and_count(arr[:mid])
    right, right_count = sort_and_count(arr[mid:])
    merged, merge_count = merge_and_count(left, right)
    
    return merged, left_count + right_count + merge_count

def count_inversions(filename):
    with open(filename, 'r') as file:
        arr = [int(line.strip()) for line in file]
    
    _, inversion_count = sort_and_count(arr)
    return inversion_count

# Assuming the file is named 'IntegerArray.txt' and is in the same directory
filename = 'IntegerArray.txt'
total_inversions = count_inversions(filename)

print(f"Total number of inversions: {total_inversions}")
