class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()
        self.tail = None

    def append_first(self,data):
        cur = self.head
        new_node = node(data)

        new_node.next = cur.next
        cur.next = new_node

        if self.tail is None:
            self.tail = new_node

    def append_last(self, data):
        new_node = node(data)

        if self.tail is None:
            self.tail = new_node
            self.head.next = self.tail

        else:
            self.tail.next = new_node
            self.tail = new_node

    def erase(self,index):
        cur = self.head
        idx = 0

        if cur.next is None:
            print("list is empty for fuck sake")

        while (cur.next != None):
            last_node = cur
            cur = cur.next

            if (idx == index):
                last_node.next = cur.next
                return

            idx += 1

    def copy_reverse(self):
        new_list = linked_list()
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            new_list.append_first(cur.data)

        return new_list


    def copy(self):
        new_list = linked_list()
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            new_list.append_last(cur.data)

        return new_list


    def display(self):
        list = []
        cur = self.head

        while cur.next != None:
            cur = cur.next
            list.append(cur.data)

        return list


my_list = linked_list()
my_list.append_first(1)
my_list.append_first(2)
my_list.append_first(3)
ans = my_list.display()
print(ans)

my_list.append_last(4)
ans = my_list.display()
print(ans)

my_list.append_last(5)
ans = my_list.display()
print(ans)

my_list.erase(2)
ans = my_list.display()
print(ans)


ans = my_list.copy_reverse()
print("this is reversed:", ans.display())

ans2 = my_list.copy()
print("this is copy:", ans2.display())