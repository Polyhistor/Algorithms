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

    def reverse(self):
        prev = None
        cur = self.head.next
        new_tail = self.head.next

        while cur is not None:
            next = cur.next
            cur.next = prev

            prev = cur
            cur = next

        # update head.next
        self.head.next = prev
         # update tail
        self.tail = new_tail

    # static
    def hasloop(self):
        old_head = self.head.next

        self.reverse()
        new_head = self.head.next

        if old_head == new_head:
            return True

        return False




my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)


test = my_list.hasloop()
print(test)

my_list.linkTailTo(2)

test2 = my_list.hasloop()
print(test2)
