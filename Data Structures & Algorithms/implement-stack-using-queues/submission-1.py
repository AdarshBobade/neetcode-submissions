from collections import deque
class MyStack:

    def __init__(self):
        self.items = deque()

    def push(self, x: int) -> None:
        self.items.append(x)
        for _ in range(len(self.items) - 1):
            self.items.append(self.items.popleft())
        
    def pop(self) -> int:
        return self.items.popleft()
        
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