# Problem Statement 

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
from typing import List

class Solution:
    def missingNumber(self, nums:List[int]) -> int:
        return sum([i + 1 for i in range(len(nums))]) - sum(nums)