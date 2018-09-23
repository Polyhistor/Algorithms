class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = new_node

    def display(self):
        cur = self.head
        list = []

        while cur.next is not None:
            cur = cur.next
            list.append(cur.data)

        return list


    def append_first(self,data):
        new_node = node(data)

        new_node.next = self.head.next
        self.head.next = new_node


    def selectionsort(self, head):
        new_list = linked_list()


        while head.next is not None:
            before_biggest = head
            biggest = head.next
            cur = head
            while cur.next is not None:
                if cur.next.data > biggest.data:
                    biggest = cur.next
                    before_biggest = cur
                cur = cur.next

            new_node = node(biggest.data)
            new_list.append_first(new_node.data)
            before_biggest.next = biggest.next

        return new_list



new_list = linked_list()
new_list.append(1)
new_list.append(2)
new_list.append(4)
new_list.append(8)
new_list.append(1)
new_list.append(-5)
new_list.append(3)
ans = new_list.display()
# print(ans)

head = new_list.head

ans = new_list.selectionsort(head)
print(ans.display())