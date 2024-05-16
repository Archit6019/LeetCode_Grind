# Problem Statement 

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

from typing import List
from collections import Counter

class Solution:
    def findDuplicate(self, nums : List[int]) -> int:
        count = Counter(nums)
        for i, j in count.items():
            if j >= 2:
                return i