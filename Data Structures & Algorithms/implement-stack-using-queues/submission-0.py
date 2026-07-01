class MyStack:

    def __init__(self):
        self.items = []
 
    def push(self, x: int) -> None:
        self.items.append(x)
        if len(self.items) > 1:
            for _ in range(len(self.items) - 1):
                for j in range(len(self.items) - 1):
                    self.items[j] , self.items[j+1] = self.items[j+1] , self.items[j]
        

    def pop(self) -> int:
        return self.items.pop(0)
        
    def top(self) -> int:
        return self.items[0]
        
    def empty(self) -> bool:
        return len(self.items) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()