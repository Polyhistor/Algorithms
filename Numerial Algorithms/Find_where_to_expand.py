def sweeper_explorer(field, numrows, numcols,  given_i, given_j):

    to_check = []

    if (field[given_i][given_j] == 0):
        field[given_i][given_j] = -2
        to_check.append(list((given_i,given_j)))

    else:
        return field

    while (to_check):

        to_check.pop()

        for i in range(given_i - 1, given_i + 2):
            for j in range(given_j - 1, given_j + 2):
                if (0 <= i <= numrows and 0 <= j <= numcols and field[i][j] == 0):
                    field[i][j] = -2


    return field



matrix = [[-1,1,0,0],
          [1,1,0,0],
          [0,0,1,1],
          [0,0,1,-1]]

ans = sweeper_explorer(matrix,3,3,1,2)
print(ans)


