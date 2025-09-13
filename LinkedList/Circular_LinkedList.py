class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end (rear)
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head   # point to itself
        else:
            temp = self.head
            while temp.next != self.head:   # go to last node
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        print(data, "inserted into circular list")

    # Delete a node
    def delete(self, key):
        if self.head is None:
            print("List is empty, cannot delete")
            return

        current = self.head
        prev = None

        # Case 1: deleting head
        if current.data == key:
            # Only one node
            if current.next == self.head:
                self.head = None
                print(key, "deleted (only node)")
                return
            # Find last node
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            print(key, "deleted from head")
            return

        # Case 2: deleting other nodes
        prev = self.head
        current = self.head.next
        while current != self.head:
            if current.data == key:
                prev.next = current.next
                print(key, "deleted from list")
                return
            prev = current
            current = current.next

        print(key, "not found in list")

    # Display list
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

cll = CircularLinkedList()

cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.insert(40)

cll.display()
# Output: 10 -> 20 -> 30 -> 40 -> (back to head)

cll.delete(10)   # delete head
cll.display()
# Output: 20 -> 30 -> 40 -> (back to head)

cll.delete(30)   # delete middle node
cll.display()
# Output: 20 -> 40 -> (back to head)
