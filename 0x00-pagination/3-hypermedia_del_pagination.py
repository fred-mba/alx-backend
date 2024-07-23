#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dict containing pagination metadata and data.

        Parameters
        ----------
        index(int): Current start index of the return page.
        page_size(int): Number of items per page.
        """
        assert isinstance(index, int) and index >= 0, \
            "index must be a non-negetive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be an integer and greater than 0"

        dataset = self.indexed_dataset()
        data = []
        current_index = index
        items_count = 0

        while items_count < page_size and current_index < len(dataset):
            item = dataset.get(current_index, None)
            if item is not None:
                data.append(item)
                items_count += 1
            current_index += 1

        next_index = current_index if current_index < len(dataset) else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
