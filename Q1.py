
arr = []

size = int(input("Enter size of array: "))

for i in range(size):
    num = int(input("Enter the elements of the array: "))
    arr.append(num)

print("Array : ", arr)

new_arr = []

for i in arr:
    if i not in new_arr:
        new_arr.append(i)

print("New array after duplicate removal : ", new_arr)


