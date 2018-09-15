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


    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # Case 1: (There's only one node)
                if not cur.next:
                    cur = None
                    self.head = None
                    return

                # Case 2: (There are two nodes)
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur.data == key:
                # Case 3: (There are many nodes ;) )
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                # Case 4: (There are many nodes ;) )
                else:
                    prev = cur.prev
                    prev.next = None
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

