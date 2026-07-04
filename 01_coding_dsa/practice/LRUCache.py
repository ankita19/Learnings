import unittest
#Implement LRU cache
'''

(prev)left(next) -> ->(prev) right(next)

insert
(prev)left(next) -> ->(prev)node(next)-> (prev) right(next)
'''

class Node:
    def __init__(self, key , val):
        self.key , self.val = key , val
        self.next , self.prev = None, None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0) , Node(0,0)

        #connect both
        self.right.prev = self.left
        self.left.next = self.right

    def remove(self, node:Node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self, node:Node):
        # hold handle of front node
        prev = self.right.prev
        next = self.right
        #add node
        prev.next = next.prev = node
        # insert node as second node from front
        node.prev = prev
        node.next = next


    def get(self, key:int):
        # if key already exist -> return value and move node to front/right
        if key in self.cache:
            # move it front and return value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key:int, val:int):
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])

        if(len(self.cache) > self.capacity):
            lru =  self.left.next
            self.remove(lru)
            del self.cache[lru.key]


class TestLRU(unittest.TestCase):
    def setUp(self):
        self.lrucache = LRUCache(3)

    def test_put_cache(self):
        """Test names should be descriptive."""
        self.lrucache.put(1, 1)
        self.lrucache.put(2, 2)
        self.lrucache.put(3, 3)
        self.assertTrue(self.lrucache.get(1) == 1)
        self.lrucache.put(1, 4)
        self.assertTrue(self.lrucache.get(1) == 4)
        self.assertTrue(len(self.lrucache.cache) == 3)


if __name__ == '__main__':
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)

    print(cache.get(1))

    cache.put(4, 4)
    #print(cache.get(1))













