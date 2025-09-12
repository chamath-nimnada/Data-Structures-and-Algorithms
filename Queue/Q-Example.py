class Queue:
    def __init__(self):
        self.items = [] # Create a List for Hold Queue Items
     
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item) # Add New Item

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) # Remove First Item
        else:
            return "Queue is empty, cannot dequeue."
        
    def peek_front(self):
        if not self.is_empty():
            return self.items[0] # Return First Item
        else:
            return "Queue is empty, no front item."
    
    def size(self):
        return len(self.items) # Return Size of Queue


# Create Object for Queue Class
q = Queue() 

# Create Objrcts for Each Functions
q.is_empty()

# New Sample Values
q.enqueue("Item 00") # Pass New Item-00
q.enqueue("Item 01") # Pass New Item-01
q.enqueue("Item 02") # Pass New Item-02

print("Queue is empty :", q.is_empty())
print("Dequeue a item :", q.dequeue()) # Remove First Item
print("Peek Front Item :", q.peek_front()) # Return First Item
print("Size of Queue :", q.size()) # Return Size of Queue