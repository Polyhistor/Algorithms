class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()
        self.tail = None

    def append(self,data):
        new_node = node(data)

        if self.tail is None:
            self.tail = new_node
            self.head.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        cur = self.head
        list = []

        while cur.next is not None:
            cur = cur.next
            list.append(cur.data)

        print(list)


    def linkTailTo(self, index):
        cur = self.head
        idx = 0

        while cur.next is not None:
            cur = cur.next
            if (index==idx):
                self.tail.next = cur
                break

            idx += 1

    def has_loop_hash(self):
        dict = {}
        cur = self.head

        while cur.next is not None:
            dict[cur] = dict.get(cur, 0) + 1
            if dict.get(cur.next) == 2:
                cur.next = None
                return True
            cur = cur.next
        return False


my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.linkTailTo(3)

ans = my_list.has_loop_hash()
print(ans)
my_list.display()