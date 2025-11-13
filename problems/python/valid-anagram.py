# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # solution 1: {}
        # for each string, create a hmap
        # key = char, val = frequency
        # if hmap_s = hmap_t return true
        # else return false

        def helper(s: str) -> dict:
            hmap = {}
            for ch in s:
                if ch in hmap:
                    hmap[ch] += 1
                else:
                    hmap[ch] = 1
            return hmap

        hmap_s = helper(s)
        hmap_t = helper(t)

        if hmap_s == hmap_t:
            return True
        else:
            return False


        # solution 2: Counter
        # from collections import Counter
        # return Counter(s) == Counter(t)
