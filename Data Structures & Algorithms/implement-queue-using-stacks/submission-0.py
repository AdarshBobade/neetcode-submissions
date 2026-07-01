class MyQueue:

    def __init__(self):
        self.stck1 = []
        self.stck2 = []
        
    def push(self, x: int) -> None:
        while self.stck1 :
            self.stck2.append(self.stck1.pop())
        self.stck1.append(x)
        while self.stck2 :
            self.stck1.append(self.stck2.pop())

    def pop(self) -> int:
        return self.stck1.pop()

    def peek(self) -> int:
        return self.stck1[-1]

    def empty(self) -> bool:
        return not self.stck1 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()