# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
#    it should invalidate the least recently used item before inserting a new item.

# class LRUCache:

#     # @param capacity, an integer
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.keys = list()
#         self.cache = dict()

#     # @return an integer
#     def get(self, key):
#         if key not in self.keys:
#             return -1
#         else:
#             value = self.cache[key]
#             self.keys.remove(key)
#             self.keys.insert(0, key)
#             return value

#     # @param key, an integer
#     # @param value, an integer
#     # @return nothing
#     def set(self, key, value):

#         l = len(self.keys)
#         if key not in self.keys:
#             if l >= self.capacity:
#                 oldkey = self.keys.pop()
#                 del self.cache[oldkey]
#             self.keys.insert(0, key)
#             self.cache[key] = value

import collections


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    # @return an integer
    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        l = len(self.cache)
        if key not in self.cache:
            if l >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value
        else:
            del self.cache[key]
            self.cache[key] = value

lrucache = LRUCache(2)
lrucache.set(2, 1)
lrucache.set(1, 1)
lrucache.set(2, 3)
lrucache.set(4, 1)
lrucache.get(1)
lrucache.get(2)
