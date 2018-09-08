class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        if self.head is None:
            new_node = node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self,data):
        if self.head is None:
            new_node = node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def display(self):
        list = []
        cur = self.head
        while cur.next:
            cur = cur.next
            list.append(cur.data)
        return list

    def add_after_node(self, data, key):
        cur = self.head
        if cur.next is None and cur.data == key:
            self.append(data)
            return
        elif cur.data == key:
            new_node = node(data)
            cur = self.head
            cur.next = new_node
            new_node.next = cur.next
            cur.next.prev = new_node
        cur = cur.next


    def add_before_node(self,data,key):
        cur = self.head
        if cur.next is None and cur.data == key:
            self.append(data)
            return
        elif cur.data == key:
            new_node = node(data)
            previ = cur.prev
            previ.next = new_node
            cur.prev = new_node
            new_node.next = cur
        cur = cur.next


    def delete(self,key):
        cur = self.head
        while cur:
            if  cur.data == key and cur == self.head:
                if cur.next is None:
                    # case 1 : we have only one node
                    cur= None
                    self.head = None
                    return
                else:
                    # case 2 : we have two nodes
                    next = cur.next
                    next.prev = None
                    cur.next = None
                    cur = None
                    self.head = next
                    return

            elif cur.data ==key:
                if cur.next:
                    # case 3 : we have too many nodes
                    next = cur.next
                    previ = cur.prev
                    next.prev = cur.prev
                    previ.next = cur.next
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                else:
                    # case 4 : we have too many nodes and we want to delete the last one
                    previ = cur.prev
                    previ.next = None
                    cur.prev = None
                    cur = None
                    return

            cur = cur.next







doubly_list = doubly_linked_list()
doubly_list.append(1)
doubly_list.append(2)
doubly_list.append(3)
ans = doubly_list.display()
print(ans)

