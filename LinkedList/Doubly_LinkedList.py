class Node:
    def __init__(self, data):
        self.data = data     # store value
        self.next = None     # pointer to next node
        self.prev = None     # pointer to previous node
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None   # start with empty list

    # Insert at front
    def insertFront(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print(data, "inserted at front")

    # Insert at end
    def insertRear(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(data, "inserted as first node")
            return
        last = self.head
        while last.next:   # go to last node
            last = last.next
        last.next = new_node
        new_node.prev = last
        print(data, "inserted at rear")

    # Delete first node
    def deleteFirst(self):
        if self.head is None:
            print("List is empty, cannot delete")
            return
        removed = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        print(removed, "deleted from front")

    # Delete last node
    def deleteLast(self):
        if self.head is None:
            print("List is empty, cannot delete")
            return
        last = self.head
        while last.next:
            last = last.next
        removed = last.data
        if last.prev:
            last.prev.next = None
        else:
            self.head = None  # only one node
        print(removed, "deleted from rear")

    # Display list forward
    def displayForward(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            last = current
            current = current.next
        print("NULL")

    # Display list backward
    def displayBackward(self):
        if self.head is None:
            print("List is empty")
            return
        # Move to last node
        current = self.head
        while current.next:
            current = current.next
        # Traverse backwards
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("NULL")

dll = DoublyLinkedList()

dll.insertFront(10)   # 10
dll.insertFront(20)   # 20 <-> 10
dll.insertRear(30)    # 20 <-> 10 <-> 30
dll.insertRear(40)    # 20 <-> 10 <-> 30 <-> 40

dll.displayForward()   # Forward: 20 <-> 10 <-> 30 <-> 40 <-> NULL
dll.displayBackward()  # Backward: 40 <-> 30 <-> 10 <-> 20 <-> NULL

dll.deleteFirst()      # Remove 20
dll.displayForward()   # Forward: 10 <-> 30 <-> 40 <-> NULL

dll.deleteLast()       # Remove 40
dll.displayForward()   # Forward: 10 <-> 30 <-> NULL
