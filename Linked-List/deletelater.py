def insertionSort(h):
    if h == None:
        return None
    #Make the first node the start of the sorted list.
    sortedList= h
    h=h.next
    sortedList.next= None
    while h != None:
        curr= h
        h=h.next
        if curr.data<sortedList.data:
            #Advance the nodes
            curr.next= sortedList
            sortedList= curr
        else:
            #Search list for correct position of current.
            search= sortedList
            while search.next!= None and curr.data > search.next.data:
                search= search.next
            #current goes after search.
            curr.next= search.next
            search.next= curr
    return sortedList

def printList(d):
    s=''
    while d:
        s+=str(d.data)+"->"
        d=d.next
    print s[:-2]

l= unorderedList()
l.add(10)
l.add(12)
l.add(1)
l.add(4)
h= l.head
printList(h)

result= insertionSort(l.head)
d= result
printList(d)