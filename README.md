1. 0x00-Pagination
- Setup: [Popular_Baby_Names.csv](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240723%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240723T143350Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7ec9e45d2e77b4c459b5fbc273a5c8c2aba969b6f44647aed088364693f42107)
0x01-Caching
* Parent class BaseCaching
- All your classes must inherit from BaseCaching defined below:
```
$ cat base_caching.py
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```
