# Finding the Median in an array

def findmedian(arr):
    n = len(arr)

    for i in range(n):
        num_larger = 0
        num_smaller = 0

        for j in range(n):
            if arr[i] < arr[j]:
                num_smaller += 1
            elif arr[i] > arr[j]:
                num_larger += 1

        if num_smaller == num_larger:
            return arr[i]



arr = [1,3,4,7,8,8,9]
ans = findmedian(arr)
print(ans)