# Problem Statement 

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        a = ''.join(sorted(s))
        b = ''.join(sorted(t))
        return a == b