class node:
    def __init__(self, data= None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()
        self.tail = None

    # def append(self, data):
    #     cur = self.head
    #     new_node = node(data)

        # while cur.next != None:
        #     cur = cur.next

        # cur.next = new_node

    def append_first(self,data):

        cur = self.head
        new_node = node(data)

        new_node.next = cur.next
        cur.next = new_node

        if self.tail is None:
            self.tail = new_node



    def append_last(self,data):

        new_node = node(data)

        if self.tail is None:
            self.tail = new_node
            self.head.next = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node



    # fix lost tail
    def erase(self,index):
        cur = self.head
        idx = 0

        while cur.next is not None:
            last_node = cur
            cur = cur.next
            if (idx  == index):
                last_node.next = cur.next
                return
            idx += 1

    # fix find biggest in empty list
    def find_biggest(self):
        cur = self.head
        largest = cur.next.data

        while cur.next is not None:
            cur = cur.next

            if ( largest < cur.data):
                largest = cur.data

        return largest

    def copy_reverse(self):
        cur = self.head
        new_list = linked_list()

        while cur.next != None:
            cur = cur.next
            new_list.append_first(cur.data)

        return new_list

    def copy(self):
        cur = self.head
        new_list = linked_list()

        while cur.next != None:
            cur = cur.next
            new_list.append_last(cur.data)

        return new_list

    def display(self):
        cur = self.head
        list=[]

        while cur.next != None:
            cur = cur.next
            list.append(cur.data)

        return list




my_list = linked_list()
my_list.append_last(1)
my_list.append_last(2)
my_list.append_last(3)
my_list.append_last(4)
ans = my_list.display()
print(ans)

ans2 = my_list.copy()
print(ans2.display())
