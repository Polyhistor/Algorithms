def mine_sweeper(bomb,row,col):

    # initializing the matrix based on given attributes
    y = [[0 for i in range(row)] for j in range(col)]

    # unpacking
    rowindex = bomb[0][0]
    colindex = bomb[0][1]

    #setting bombs
    y[rowindex][colindex] = -1

    print("bombs:", y)

    #looping through
    for i in range(rowindex - 1, rowindex + 2):
        for j in range(colindex - 1, colindex + 2):
            if (0 <= i <= row and 0 <= j <= col and y[i][j] != -1):
                y[i][j] += 1


    return y


bombs = [[0,0]]
ans = mine_sweeper(bombs,3,4)
print("final result",ans)