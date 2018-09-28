class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None

class linked_list:
    def __init__(self):
        self.head = node()
        self.tail = node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def append_last(self,data):
        new_node = node(data)


        new_node.next = self.tail
        tail_prev = self.tail.prev
        new_node.prev = tail_prev

        self.tail.prev = new_node
        tail_prev.next = new_node



    def display(self):
        list = []
        cur = self.head

        while cur.next is not self.tail :
            cur = cur.next
            list.append(cur.data)

        return  list


    def delete(self,index):

        cur = self.head
        idx = 0

        while cur.next is not None:
            cur = cur.next
            if (idx == index):
                remove = cur
                before_remove = cur.prev
                after_remove = cur.next

                before_remove.next = remove.next
                after_remove.prev = remove.prev

            idx += 1


    def is_sorted(self):

        cur = self.head

        while cur.next is not self.tail:
            cur = cur.next

            if cur.next != self.tail and cur.next.data < cur.data:
                return False


        return True



my_list = linked_list()
my_list.append_last(1)
my_list.append_last(2)
my_list.append_last(3)

# ans = my_list.display()
# print(ans)
#
#
# my_list.delete(1)
# ans = my_list.display()
# print(ans)


ans = my_list.is_sorted()
print(ans)