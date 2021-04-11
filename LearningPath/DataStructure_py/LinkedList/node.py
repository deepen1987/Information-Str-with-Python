class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    __size = 0

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
        self.__size += 1

    def add_last(self, lili):
        if self.head is None:
            self.head = lili
            self.tail = lili
        else:
            self.tail.next = lili
            self.tail = lili
        self.__size += 1

    def delete_first(self):
        if self.head is None:
            print("Not Enough Nodes")
            self.__size = 0
        elif self.head.next is None:
            self.head = None
            self.tail = None
            self.__size = 0
        else:
            self.head = self.head.next
            self.__size -= 1

    def delete_last(self):
        if self.head is None:
            print("Not Enough Nodes")
            self.__size = 0
        elif self.head.next is None:
            self.head = None
            self.tail = None
            self.__size = 0
        else:
            node_check = True
            while node_check:
                prev = self.head
                nex = self.head.next
                if nex.next is None:
                    prev.next = None
                    self.tail = prev
                    node_check = False
            self.__size -= 1

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

    def getsize(self):
        return self.__size

    # Reverse a linked list in same position
    def reverse_lili(self):
        if self.head is None:
            return
        # rev = True
        # while rev:
        #     current = self.head
        #     nex = self.head.next
        #     while nex.next:
        #         current = current.next
        #         nex = nex.next
        #     nex.next = current
        #     current.next = None
        #     if self.head.next is None:
        #         self.head = self.tail
        #         self.tail = nex.next
        #         current = None
        #         rev = False

        prev = self.head
        current = prev.next
        while current.next:
            nex = current.next
            current.next = prev
            prev = current
            current = nex

        self.tail = self.head
        self.tail.next = None
        self.head = prev

    def lili_values(self):
        current = self.head
        out = []
        while current.next:
            out.append(current.data)
            current = current.next
        return out

    def get_kth_node_end(self, k):
        if self.head is None or k < 1:
            return "Empty Linked List"
        first = self.head
        second = self.head
        for i in range(k-1):
            second = second.next
            if second is None:
                return "K is bigger then the list"
        while second.next is not None:
            first = first.next
            second = second.next
        return first.data

lLIns = LinkedList()
print(lLIns.getsize())
lLIns.add_first(Node(4))
print(lLIns.getsize())
lLIns.add_first(Node(5))
lLIns.add_last(Node(7))
print(lLIns.getsize())
lLIns.delete_first()
print(lLIns.getsize())
lLIns.delete_first()
lLIns.delete_last()
lLIns.delete_last()
print(lLIns.getsize())
lLIns.add_first(Node(8))
print(lLIns.getsize())
lLIns.contains(7)
print(lLIns.index_of(4))
print(lLIns.lili_values())
print(lLIns.get_kth_node_end(int(input())))
