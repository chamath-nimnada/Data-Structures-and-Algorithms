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
            print(item, "Pushed to Stack")

    def pop(self):
        if self.is_empty():
            return "Stack Underflow, cannot pop."
        else:
            item = self.stack[self.top]
            self.stack[self.top] = None # Clear the position
            self.top -= 1
            print(item, "Popped from Stack")
            return item # Remove Top Item

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
s.pop() # Remove Top Item