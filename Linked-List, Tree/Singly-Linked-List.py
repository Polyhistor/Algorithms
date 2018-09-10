class node:
    def __init__(self, data=None):
        self. data = data
        self.next = None

class linked_list:

    def __init__(self):
        self.head = node()

    def append(self,data):
        cur = self.head
        new_node = node(data)

        while cur.next is not None:
            cur = cur.next

        cur.next = new_node

    def display(self):
        cur= self.head
        list = []

        while (cur.next!=None):
            cur = cur.next
            list.append(cur.data)

        print(list)

    def length(self):
        cur = self.head
        total = 0

        while (cur.next!=None):
            cur = cur.next
            total += 1
        return total

    def get_index(self,index):
        if(index >= self.length()):
            print("out of range!")
            return None

        cur=self.head
        idx = 0

        while True:
            cur = cur.next
            if(idx == index):
                return cur.data
            idx += 1

    def erase (self,index):
        if(index >= self.length()):
            print("out of range!")
            return None

        cur=self.head
        idx = 0

        while True:
            last_node = cur
            cur = cur.next
            if (idx == index):
                last_node.next = cur.next
                return
            idx += 1


    def add_beginning(self,data):
        cur = self.head
        new_node = node(data)

        new_node.next = cur.next
        cur.next = new_node

    def cell_after_cell(self,afterme,data):
        cur= self.head
        new_node = node(data)
        idx = 0

        while(cur.next!=None):
            cur = cur.next
            if (idx==afterme):
                afterme = cur
                new_node.next = afterme.next
                afterme.next = new_node
            idx +=1



my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.display()
my_list.length()

idx = my_list.get_index(0)
print(idx)

# my_list.erase(0)

my_list.display()
my_list.add_beginning(4)
my_list.display()


my_list.cell_after_cell(2,10)
my_list.display()