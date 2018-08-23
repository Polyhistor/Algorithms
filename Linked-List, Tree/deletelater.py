class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        cur = self.head
        new_node = node(data)
        while(cur.next!=None):
            cur = cur.next
        cur.next = new_node

    def display(self):
        list = []
        cur = self.head
        while(cur.next!=None):
            cur = cur.next
            list.append(cur.data)
        print(list)

    def length(self):
        total = 0
        cur = self.head
        while(cur.next!=None):
            cur = cur.next
            total += 1
        return total

    def get(self, index):
        if (index >= self.length()):
            print("out of range you fuck")
        cur = self.head
        idx = 0
        while True:
            cur = cur.next
            if (idx == index):
                return cur.data
            idx += 1

    def erase(self, index):
        if (index >= self.length()):
            print("out of range you fuck")
        cur=self.head
        idx = 0
        while True:
            last_node = cur
            cur = cur.next
            if(idx == index):
                cur.next = last_node.next
            idx += 1

my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.display()
print(my_list.get(0))
print(my_list.length())
my_list.erase(0)
my_list.display()

