#!/usr/bin/env python3
""" Create a class BasicCache that inherits from BaseCaching
    and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basic cache"""
    def __init__(self):
        """init """
        super().__init__()

    def put(self, key, item):
        """put"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """get"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
