# Remove and index from an array

def removeitem(arr,index):

    n = len(arr)

    for i in range(index, n-1):
        arr[i] = arr[i+1]

    arr.pop()


arr = [1,2,3,4]
removeitem(arr,1)
print(arr)

# 1 to 10  lowerBoundE = 1
# 2000 to 2010 lowerBoundY = 2000
# sales [1][2000] = 20123 [0][0]
# sales [2 - lowerBoundE][2009 - lowerBoundY] = 2123123 [1][9]

