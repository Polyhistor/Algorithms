# Finding the minimum

def minimum(arr):
    minimum = arr[0]

    for i in range(len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]


    return minimum



arr = [4,5,6,3,2,1]
ans = minimum(arr)
print(ans)


