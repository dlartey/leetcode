class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.table = collections.defaultdict()
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self,node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        # RETURN -1 if key isn't in table, or the key isn't within the boundaries of the size
        if (key in self.table):
            self.remove(self.table[key])
            self.insert(self.table[key])
            return self.table[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.table:
           self.remove(self.table[key])
        self.table[key] = Node(key,value)
        self.insert(self.table[key])
        
        if len(self.table) > self.size:
            lru = self.left.next
            self.remove(lru)
            del self.table[lru.key]

class Node:
    def __init__(self, key,val):
        self.key, self.val = key,val
        self.prev, self.next = None, None

    
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)