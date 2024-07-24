#!/usr/bin/env python3
"""
LFU caching module
"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ Least Frequently Used cache class """
    def __init__(self):
        """Initialize the cache.
            - self.frequecy: Track access frequencies
            - self.frequency_order: Track order of items for each frequency
            - self.min_frequency: Track the minimum frequency
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.freq_order = defaultdict(OrderedDict)
        self.min_freq = 0

    def put(self, key, item):
        """- If key exists in the cache, update value of existing item.
           - Else if the cache is full evict the least freq used item.
           - Add  the new item to `self.cache_data` and update `self.frequency`
            and `self.freq_order`
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_frequency(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict()

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.freq_order[1][key] = None
            self.min_freq = 1

    def get(self, key):
        """Get an item by key.
            - If key exists update its frequency and return the value
            - Else, return `None`.
        """
        if key is None or key not in self.cache_data:
            return None

        self._update_frequency(key)
        return self.cache_data[key]

    def _update_frequency(self, key):
        """Update key frequency access.
            - Remove the `key` from its current freq_order.
            - Increment the freq of the `key`
            - Add the key to the new frequency order
        """
        freq = self.frequency[key]
        del self.freq_order[freq][key]

        if not self.freq_order[freq]:
            del self.freq_order[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        self.frequency[key] += 1
        freq = self.frequency[key]
        self.freq_order[freq][key] = None

    def _evict(self):
        """Evict the least freq used item. If there are multiple items with the
           same frequency, evict the least recently used(LRU) one.
        """
        key, _ = self.freq_order[self.min_freq].popitem(last=False)
        if not self.freq_order[self.min_freq]:
            del self.freq_order[self.min_freq]
        del self.cache_data[key]
        del self.frequency[key]
        print(f"DISCARD: {key}")
