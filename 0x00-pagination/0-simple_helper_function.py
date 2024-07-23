#!/usr/bin/env python3
"""
This module calculates the start and end indexes for pagination
and returns a tuple containing start and end index.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Parameters
    ----------
    page(int): Current page number
    page_size(int): The number of items per page
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
