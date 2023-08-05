class MinStack:
    #constructor
    def __init__(self):
        # initialise empty stack
        self.stack = []
        self.minStack = []
    # push to stack
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        # append val to minStack
        self.minStack.append(val)
        return self.stack
    # pop from stack    
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
        


# Your MinStack object will be instantiated and called as such:
val = 1
obj = MinStack()
print(obj.push(val))
print(obj.push(2))

# print(obj.pop())
param_3 = obj.top()
param_3
param_4 = obj.getMin()
param_4
