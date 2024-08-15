source = [1, 2, 5, 4, 3]
source = [1, 2, 5, 4, 3, 8, 6, 7, 10, 0, 12]

def quick_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
        
    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)
        
def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

quick_sort(source)     
print(source)
