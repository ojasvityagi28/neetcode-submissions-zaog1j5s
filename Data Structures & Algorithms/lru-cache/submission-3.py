class Node:
    def __init__(self, key ,value , left = None , right = None) -> None:
        self.key = key
        self.value = value
        self.prev = left
        self.next = right
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.keyTonode = {}
        self.first = Node(0 , 0, None, None)
        self.last = Node(0 , 0, None, None)
        self.first.next = self.last
        self.last.prev = self.first

    def addToBeginning(self , node: Node):
        tmp = self.first.next
        self.first.next = node
        tmp.prev = node
        node.prev, node.next = self.first , tmp
    
    def remove(self , node : Node):
        second_last = node
        second_last.prev.next = second_last.next
        second_last.next.prev = second_last.prev
        return node
 
    def get(self, key: int) -> int:
        if key in self.keyTonode:
            node = self.keyTonode[key]
            self.remove(node)
            self.addToBeginning(node)
            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.keyTonode:
            node = self.keyTonode[key]
            node.value = value
            self.remove(node)
            self.addToBeginning(node)

        elif len(self.keyTonode) == self.size:
            node = self.remove(self.last.prev)
            del self.keyTonode[node.key]
            node = Node(key ,value)
            self.keyTonode[key] = node
            self.addToBeginning(node)
        else:
            node = Node(key ,value)
            self.keyTonode[key] = node
            self.addToBeginning(node)


        
