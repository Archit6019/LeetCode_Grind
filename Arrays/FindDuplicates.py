# Problem Statement 

# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

from collections import Counter
from typing import List

class Solution:
    def findDuplicates(self, nums : List[int]) -> List[int]:
        count = Counter(nums)
        output = []
        for i , j in count.items():
            if j == 2:
                output.append(i)

        return output