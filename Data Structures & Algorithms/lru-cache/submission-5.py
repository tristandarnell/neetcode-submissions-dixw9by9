class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev, self.next = None, None

class LRUCache:  

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right

    def remove(self, node):
        prev_node = node.prev
        nxt_node = node.next

        prev_node.next = nxt_node
        nxt_node.prev = prev_node


    
    def insert(self, node):
        prev_node = self.right.prev
        nxt_node = self.right

        prev_node.next = node
        nxt_node.prev = node

        node.prev = prev_node
        node.next = nxt_node
    


        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
