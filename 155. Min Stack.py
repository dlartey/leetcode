class MinStack:
    
    def __init__(self):
        self.stack = []
        # stored as a (val,minSoFar) combination

    def push(self, val: int) -> None:
        if (len(self.stack) == 0):
            self.stack.append((val,val))
        else:
            newMin = min(self.stack[-1][1],val)
            self.stack.append((val,newMin))
        
        # if length of stack is empty, then init
      
    def pop(self) -> None:
        self.stack.pop()
       
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
      
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()