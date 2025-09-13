class Node:
    def __init__(self, data):
        self.data = data # Store Data
        self.next = None # Pointer to Next Node (None = End)

class LinkedList:
    def __init__(self):
        self.head = None # Start with empty list

    # Insert at front of the list
    def insertFront(self, data):
        new_node = Node(data) # Create New Node
        new_node.next = self.head # New Node points to current head
        self.head = new_node # Update head to new node
        print(data, "inserted at the front.")

    # Insert at end of the list
    def insertRear(self, data):
        new_node = Node(data)
        if self.head is None: # If list is empty
            self.head = new_node # New node becomes head
            print("1st Node Added: ", data)
            return
        last = self.head
        while last.next: # Move to last node
            last = last.next
        last.next = new_node # Link last node to new node
        print(data, "inserted at the End.")

    def displayList(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current: # Traverse the list
            print(current.data, end=" -> ")
            current = current.next
        print("Null")

     # Delete first node
    def deleteFirst(self):
        if self.head is None:
            print("List is empty, cannot delete")
            return
        removed = self.head.data
        self.head = self.head.next   # move head to next node
        print(removed, "deleted from front")

ll = LinkedList() # Create Object for LinkedList Class

# Insert Node with Data
ll.insertFront("Node 1") 
ll.insertFront("Node 2")

ll.insertRear("Node 3")
ll.insertRear("Node 4")

ll.displayList() # Display the Linked List

ll.deleteFirst()     # Remove Node 2
ll.displayList()