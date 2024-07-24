#!/usr/bin/env python3
"""
MRU caching module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Most Recently Used Cache class
    """
    def __init__(self):
        """Initialize the cache. self.mru_stack to track the order of usage
        """
        super().__init__()
        self.mru_stack = []

    def put(self, key, item):
        """Add an item in the cache
           - If key already in cache, it removes `key` from `self.mru_stack`
            prints the `DISCARD` message and removes the item from
            self.cache_data
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.mru_stack.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.mru_stack.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.mru_stack.append(key)

    def get(self, key):
        """Get an item by key
           - Updates the position of `key` in `self.mru_order` to mark it as
            recently used.
        """
        if key is None or key not in self.cache_data:
            return None

        self.mru_stack.remove(key)
        self.mru_stack.append(key)

        return self.cache_data.get(key)
