class node:
    def __init__(self, data=None):
        self.data = data
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

    def sort_append(self, data):
        cur = self.head
        new_node = node(data)

        while cur.next is not None and cur.next.data < new_node.data:
            cur = cur.next

        new_node.next = cur.next
        cur.next = new_node


    def display(self):
        list = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            list.append(cur.data)
        return list


my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.sort_append(1)

ans = my_list.display()
print(ans)