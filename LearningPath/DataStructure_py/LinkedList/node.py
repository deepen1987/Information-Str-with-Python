class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, lili):
        if self.head is None:
            self.head = lili
            self.tail = lili
        else:
            lili.next = self.head
            self.head = lili

    def add_last(self, lili):
        if self.head is None:
            self.head = lili
            self.tail = lili
        else:
            self.tail.next = lili
            self.tail = lili

    def delete_first(self):
        if self.head is None:
            print("Not Enough Nodes")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            print("Not Enough Nodes")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            node_check = True
            while node_check:
                prev = self.head
                nex = self.head.next
                if nex.next is None:
                    prev.next = None
                    self.tail = prev
                    node_check = False

    def contains(self, value):
        cur = self.head
        data_check = True
        while data_check:
            if cur.data == value:
                return True
            elif cur.next is None:
                return False
            else:
                cur = cur.next

    def index_of(self, value):
        cur = self.head
        data_check = True
        counter = 0
        while data_check:
            if cur.data == value:
                return counter
            elif cur.next is None:
                return False
            else:
                cur = cur.next
                counter += 1


lLIns = LinkedList()
lLIns.add_first(Node(4))
lLIns.add_first(Node(5))
lLIns.add_last(Node(7))
lLIns.delete_first()
lLIns.delete_first()
lLIns.delete_last()
lLIns.delete_last()
lLIns.add_first(Node(8))
lLIns.contains(7)
print(lLIns.index_of(4))
