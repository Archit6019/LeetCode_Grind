# Problem Statement 

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

from typing import List 

class Solution:
    def twoSum(self, nums : List[int], target : int) -> List[int]:
        n = len(nums)
        hash_map = {}

        for i in range(n):
            complement = target - nums[i]
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[nums[i]] = i 