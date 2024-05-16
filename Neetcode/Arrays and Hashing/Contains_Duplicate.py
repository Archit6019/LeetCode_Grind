# Problem Statement 

#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

from typing import List 
from collections import Counter 

class Solution:
    # Approach 1 (Using Hash map)

    def containsDuplicate_hm(self, nums:List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True 
            seen[num] = seen.get(num, 0) + 1
        return False 
    
    # Approach 2 (Using Counter)

    def containsDuplicate_c(self, nums:List[int]) -> bool:
        count = Counter(nums)
        max_value = max(count.values())
        return max_value > 1


