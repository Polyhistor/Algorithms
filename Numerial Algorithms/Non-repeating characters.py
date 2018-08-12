# Finding most-repeating character

#Part 1 - Just findin the most occurring character

def mostoccur(arr):

    n = len(arr)
    dict={}

    for i in range(n):
        dict[arr[i]] = dict.get(arr[i],0) + 1


    return dict


string = "aabbcccccdddddddd"
ls = list(string)
ans = mostoccur(ls)

print("The dictionary of all the characters and their frequency: \n",ans)

maximum = max(ans)
print("\nThe most occuring character is:",maximum)



# Part 2 - Alright, now let's find the second most occurring character

biggest = {'most-occuring':0, 'second-most-occuring':0}

for a in ans.items():
    for b in ans.items():
        if a < b:
            a,b = b,a
            biggest['most-occuring'] = a
            biggest['second-most-occuring']= b



print(biggest)

