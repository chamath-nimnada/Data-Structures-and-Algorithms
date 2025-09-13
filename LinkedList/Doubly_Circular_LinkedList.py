class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            last = self.head.prev    # last node (because head.prev points to last)
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node
        print(data, "inserted into doubly circular list")

    # Delete a node
    def delete(self, key):
        if self.head is None:
            print("List is empty, cannot delete")
            return

        current = self.head
        found = False

        while True:
            if current.data == key:
                found = True
                break
            current = current.next
            if current == self.head:  # full loop
                break

        if not found:
            print(key, "not found in list")
            return

        # If only one node
        if current.next == current and current.prev == current:
            self.head = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            if current == self.head:
                self.head = current.next
        print(key, "deleted from list")

    # Display forward
    def displayForward(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

    # Display backward
    def displayBackward(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head.prev   # start at last node
        while True:
            print(current.data, end=" <-> ")
            current = current.prev
            if current.next == self.head:  # looped back
                print(current.data, end=" <-> ")
                break
        print("(back to head)")

dcll = DoublyCircularLinkedList()

dcll.insert(10)
dcll.insert(20)
dcll.insert(30)
dcll.insert(40)

dcll.displayForward()
# Output: 10 <-> 20 <-> 30 <-> 40 <-> (back to head)

dcll.displayBackward()
# Output: 40 <-> 30 <-> 20 <-> 10 <-> (back to head)

dcll.delete(10)   # delete head
dcll.displayForward()
# Output: 20 <-> 30 <-> 40 <-> (back to head)

dcll.delete(30)   # delete middle node
dcll.displayForward()
# Output: 20 <-> 40 <-> (back to head)
