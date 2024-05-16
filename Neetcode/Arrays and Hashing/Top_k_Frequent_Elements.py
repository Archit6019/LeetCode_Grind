# Problem Satement 

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from collections import Counter
from typing import List 

class Solution:
    def topKFrequent(self, nums : List[int], k:int) -> List[int]:
        count = Counter(nums)
        sorted_count = dict(sorted(count.items(), key=lambda item : item[1], reverse=True))
        return list(sorted_count.keys())[:k]