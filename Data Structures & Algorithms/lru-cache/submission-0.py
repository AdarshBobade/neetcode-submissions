class Node:
    def __init__(self,key,val):
        self.key , self.val = key,val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key and Nodes 

        #lru = Least Recently used and mru = Most recently used
        # everytime we carry an operation lets sat get or put that particular node becomes Most recently used .
        self.lru , self.mru = Node(0,0) , Node(0,0)
        self.lru.next , self.mru.prev = self.mru , self.lru

    #remove from lru
    def remove(self,node):
        prev , nxt = node.prev , node.next
        prev.next ,nxt.prev = nxt , prev
        

    #insert at mru (rightmost)
    def insert(self,node):
        prev , nxt = self.mru.prev , self.mru
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    # if we get a value that particular node becomes mru !so we remove and insert it at rightmost position(mru position)    
    def get(self, key: int) -> int:
        if key in self.cache :
            # we have to put this (key,val) into mru
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache :
            self.remove(self.cache[key])

        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap :
            #remove from the lru
            lru_node = self.lru.next
            self.remove(lru_node)
            del self.cache[lru_node.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)