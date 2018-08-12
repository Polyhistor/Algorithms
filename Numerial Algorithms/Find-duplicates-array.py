
def find_duplicates(arr):

    n = len(arr)
    duplicate = []

    for i in range(n):
        for j in range(i+1,n):
            if (arr[i] == arr[j]):
                duplicate.append(arr[i])


    return duplicate


arr = [1,2,3,2,5,6]
ans = find_duplicates(arr)
print(ans)
