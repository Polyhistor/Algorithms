#inserting items

def insertitem(arr,index, value):

    arr.append(None)
    n = len(arr)

    for i in range(n-1, index, -1):
        arr[i] = arr[i-1]

    arr[index] = value




arr = [1,2,3,4]
print(arr)
insertitem(arr,2,6)
print(arr)

