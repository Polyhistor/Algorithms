# finding the average

def findaverage(arr):
    total = 0
    n = len(arr)

    for i in range(n):
        total += arr[i]


    return total/n


arr = [2,3,5]
ans = findaverage(arr)
print(ans)

