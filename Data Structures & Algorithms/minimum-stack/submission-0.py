class MinStack:

    def __init__(self):
        self.items = []
   
    def push(self, val: int) -> None:
        if len(self.items) == 0:
            self.items.append([val,val])
        else :
            new_min = min(val , self.items[-1][-1])
            self.items.append([val , new_min])
        
    def pop(self) -> None:
        return self.items.pop()
        
    def top(self) -> int:
        return self.items[-1][0]
    
    def getMin(self) -> int:
        return self.items[-1][-1]
        
