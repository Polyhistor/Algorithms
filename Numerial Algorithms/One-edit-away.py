def on_edit_away(str1, str2):

    if len(str1) < len(str2):
        return on_edit_away(str2, str1)

    counter = 0
    j = 0

    for i in range(len(str1)):
        print("this is I", i)
        print("this is J", j)
        if(j == len(str2)):
            counter +=1
        elif (str1[i] != str2[j]):
            counter += 1
        else:
            j += 1



    if counter > 1 :
        print("its not one edit away")

    else:
        print(counter)
        print("one edit away!")


str = "ab"
str2 = "abc"

ans=on_edit_away(str,str2)
print(ans)
