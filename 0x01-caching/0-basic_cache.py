#!/usr/bin/env python3
""" Inherits from base_caching.py module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching system with no limit
    """
    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
