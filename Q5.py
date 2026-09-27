
arr = []
n = int(input("Enter array size: "))

for i in range(n):
    num = int(input("Enter elements : "))
    arr.append(num)

target = int(input("Element to be searched: "))

def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])

    left = merge_sort(arr1)
    right = merge_sort(arr2)

    return merge(arr, left, right)


def merge(arr : list[int], arr1, arr2):

    merged = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr2[j])
            i += 1
        else: 
            merged.append(arr2[j])
            j += 1
        
    if i < len(arr1):
        merged.extend(arr1[i:])
    if j < len(arr):
        merged.extend(arr2[j:])

    return merged 

ans = merge_sort(arr)
print("Sorted array: ", ans) 

def binary_search(arr, low, high, target):
    
    if low > high:
        return -1
    
    mid = (low + high)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, mid + 1,  high, target)
    else:
        return binary_search(arr, low, mid - 1, target )
    

ans = binary_search(arr, 0, len(arr)-1, target)
print(ans)
