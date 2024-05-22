# Problem Statement 

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

from typing import List

class Solution:
    def longestConsecutive(self, nums : List[int]) -> int:
        if not nums:
            return 0 
        
        num_set = set(nums)
        count = 0 

        for i in num_set:
            if i - 1 not in num_set:
                current = i 
                current_count = 1 

                while current + 1 in num_set:
                    current += 1 
                    current_count += 1 

                count = max(count, current_count)

        return count 