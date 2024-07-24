#!/usr/bin/env python3
"""
LIFO caching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache class
    """
    def __init__(self):
        """Initialize the cache
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            newest_key = self.stack.pop()
            del self.cache_data[newest_key]
            print(f"DISCARD: {newest_key}")

        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
