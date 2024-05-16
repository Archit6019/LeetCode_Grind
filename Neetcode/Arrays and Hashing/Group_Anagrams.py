# Problem Statement 

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
from typing import List

class Solution:
    def group_anagrams(self, strs:List[str]) -> List[List[str]]:
        hash_map = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in hash_map:
                hash_map[sorted_string].append(string)
            else:
                hash_map[sorted_string] = [string]

        return list(hash_map.values())
    
    