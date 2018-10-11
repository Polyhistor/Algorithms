# Find Maximum

def findmaximum(arr):
    maximum = arr[0]

    for i in range(len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]

    return maximum



arr = [3,4,1,6,2,9]
ans = findmaximum(arr)
print(ans)