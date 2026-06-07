class LRUCache:
    class Node:
        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}  # key -> Node

        # Sentinel head and tail (dummies avoid edge cases)
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Detach node from wherever it is."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node):
        """Insert node right after head (MRU position)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)        # pull out
        self._insert_front(node)  # push to MRU
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
        node = self.Node(key, value)
        self.map[key] = node
        self._insert_front(node)

        if len(self.map) > self.cap:
            # LRU is just before the tail sentinel
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]