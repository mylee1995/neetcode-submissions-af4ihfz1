class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.before = None
        self.after = None
    

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # Initialize double linked liist
        self.LRU = Node(0,0)
        self.MRU = Node(0,0)
        self.LRU.after = self.MRU
        self.MRU.before = self.LRU

        # Initialize map {key : Node(val)}
        self.obj = {}    

    def get(self, key: int) -> int:
        if key not in self.obj:
            return -1
        node = self.obj[key]
        self.removeNode(node)
        self.appendToMRU(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        # if key exists, remove the old node and append the new node to MRU
        if key in self.obj:
            self.removeNode(self.obj[key])
            node = Node(key, value)
            self.appendToMRU(node)
            self.obj[key] = node
        # else key does not exist, check capacity 
        else:
            node = Node(key, value)
            self.appendToMRU(node)
            self.obj[key] = node
            if len(self.obj) > self.capacity:
                currLRU = self.LRU.after
                self.removeNode(currLRU)
                del self.obj[currLRU.key]

    def removeNode(self, node: Node) -> None:
        prev = node.before
        after= node.after
        prev.after = after
        after.before = prev

    def appendToMRU(self, node: Node) -> None:
        currMRU = self.MRU.before
        currMRU.after = node
        node.before = currMRU
        node.after = self.MRU
        self.MRU.before = node

