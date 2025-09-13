class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size # Create a List for Hold Stack Items
        self.top = -1 # Initialize Top of Stack

    def is_empty(self):
        return self.top == -1 

    def is_full(self):
        return self.top == self.size - 1

    def push(self, item):
        if self.is_full():
            print("Stack Overflow, cannot push:", item)
        else:
            self.top += 1
            self.stack[self.top] = item # Add New Item
            print("Pushed: ", item)

    def pop(self):
        if self.is_empty():
            return "Stack Underflow, cannot pop."
        else:
            item = self.stack[self.top]
            self.stack[self.top] = None # Remove the top item
            self.top -= 1 # Decrease Top index
            return item 

    def peek(self):
        if self.is_empty():
            return "Stack is empty, no top item."
        else:
            return self.stack[self.top] # Return Top Item

s = Stack(5) # Create Object for Stack Class with Size 5

s.push("Plate 1")
s.push("Plate 2")
s.push("Plate 3")

print("Stack is empty :", s.is_empty())
print("Popped Item :", s.pop()) # Remove Top Item