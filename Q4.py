arr = []

size = int(input("Enter size of element: "))

for i in range(size):
    num = int(input("Enter elements of the array: "))
    arr.append(num)


def arr_sum(arr : list[int], index  : int) -> int:

    if index == -1:
        return 0
    
    return arr[index] + arr_sum(arr, index + 1)

ans : int = arr_sum(arr, len(arr) - 1)

print(ans)



