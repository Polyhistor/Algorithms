class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.visited = False

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

    def linkTailTo(self, index):
        cur = self.head
        idx = 0

        while cur.next is not None:
            cur = cur.next
            if (index==idx):
                self.tail.next = cur
                break

            idx += 1


    def hasloop(self):
        cur = self.head
        has_loop = False

        while cur.next is not None:             # O(n)
            if cur.next.visited:
                has_loop = True
                break
            cur = cur.next
            cur.visited = True


        cur.next = None
        cur = self.head
        while cur.next is not None:            # O(n)
            cur = cur.next
            cur.visited = False

        return has_loop

        # total = 2 x O(n) = O(n)

    def display(self):
        list = []
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            list.append(cur.data)

        print(list)



my_list = linked_list()
my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

ans2 = my_list.hasloop()
my_list.linkTailTo(2)
ans2 = my_list.hasloop()
print(ans2)
my_list.display()
