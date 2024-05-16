# Problem Statement 

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Approach = XORing a number with itself results in 0, and XORing a number with 0 results in the number itself. Therefore, if you XOR all the numbers in the array, the duplicates will cancel out, leaving only the single number that appears once.
from typing import List 


class Solution:
    def singleNumber(self, nums : List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result