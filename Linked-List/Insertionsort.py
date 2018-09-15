class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()
        self.tail = None

    def append(self, data):
        cur = self.head
        new_node = node(data)

        while cur.next != None:
            cur = cur.next

        cur.next = new_node

    def display(self):
        cur = self.head
        list = []

        while cur.next != None:
            cur = cur.next
            list.append(cur.data)

        return list


    def insertionsort(self,head):

        sorted_list = linked_list()
        cur = head.next

        while cur is not None:
            new_node = node(cur.data)
            afterme = sorted_list.head

            while afterme.next is not None and new_node.data > afterme.next.data:
                afterme = afterme.next

            new_node.next = afterme.next
            afterme.next = new_node

            cur = cur.next

        return sorted_list





my_list = linked_list()
my_list.append(4)
my_list.append(1)
my_list.append(15)
my_list.append(22)
my_list.append(10)

# ans = my_list.display()
# print(ans)

head = my_list.head

sorted = my_list.insertionsort(head)
print(sorted.display())

# select = my_list.selectionsort(head)
