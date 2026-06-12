
class MyHashMap:

    def __init__(self):
        self.size = 10007
        self.buckets = [[] for x in range(self.size)]
    
    def hash(self,key):
        # key = 
        return key % self.size
        

    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        for i , (k,v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key,value)
                return
        self.buckets[idx].append((key,value))
        

    def get(self, key: int) -> int:
        idx = self.hash(key)
        for k , v in self.buckets[idx]:
            if k == key:
                return v 
        return -1
        

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        self.buckets[idx] = [(k, v) for k, v in self.buckets[idx] if k != key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)