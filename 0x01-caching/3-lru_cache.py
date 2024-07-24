#!/usr/bin/env python3
"""
LRU caching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Least Recently Used Cache class
    """
    def __init__(self):
        """Initialize the cache
           self.lru_order: Tracks the order of usage with the least used item
           at the beginning
        """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """Add an item in the cache
           - If key already in cache, it removes `key` from `self.lru_order`
            prints the `DISCARD` message and removes the item from
            self.cache_data
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.lru_order.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.lru_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.lru_order.append(key)

    def get(self, key):
        """Get an item by key
           - Updates the position of `key` in `self.lru_order` to mark it as
            recently used.
        """
        if key is None or key not in self.cache_data:
            return None

        self.lru_order.remove(key)
        self.lru_order.append(key)

        return self.cache_data.get(key)
