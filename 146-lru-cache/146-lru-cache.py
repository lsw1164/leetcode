class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None
    
    
class LinkedList:
    def __init__(self):
        self.dummy = self.tail = Node(None, None)
        self.size = 0
        
    def add_front(self, new_node):
        if self.dummy == self.tail: self.tail = new_node
        front = self.dummy.next
        new_node.prev = self.dummy
        self.dummy.next = new_node
        if front: front.prev = new_node
        new_node.next = front
        self.size += 1
        
    def extract(self, node):
        prev_node = node.prev
        next_node = node.next
        if node == self.tail: self.tail = prev_node
        prev_node.next = next_node
        if next_node: next_node.prev = prev_node
        self.size -= 1
        node.prev = node.next = None
        return node
        
    def travel(self):
        cur = self.dummy.next
        sb = ""
        while cur:
            sb += f"(key:{cur.key},val:{cur.val}) "
            cur = cur.next
        print(sb)
        
        
class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.llist = LinkedList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.llist.extract(node)
        self.llist.add_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.get(key)
            return
        new_node = Node(key, value)
        self.llist.add_front(new_node)
        self.map[key] = new_node
        if self.llist.size > self.capacity:
            oldest = self.llist.extract(self.llist.tail)
            del self.map[oldest.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)