from multiprocessing import Pool
from typing import List

def add_lists(lists: List[List[int]]) -> List[int]:
    with Pool() as pool:
        results = pool.map(sum, lists)
    return results
