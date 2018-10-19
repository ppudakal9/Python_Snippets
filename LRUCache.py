from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.lru_cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.lru_cache:
            return self.lru_cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.lru_cache:
            self.lru_cache.pop(key)
            self.lru_cache[key] = value

        elif len(self.lru_cache) == self.capacity:
            self.lru_cache.popitem(last=False)

        self.lru_cache[key] = value