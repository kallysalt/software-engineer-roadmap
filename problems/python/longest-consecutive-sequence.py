# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # edge cases: empty list, list with one element, ...

        # solution 1: sort + count (brute force)
        
        # solution 2: 

        # store elements in a set for quick lookup
        # then use a while loop to cnt length of the sequence
        numSet = set(nums)
        res = 0

        for num in numSet:
            # identify the start point (very trickky to get it right)
            if (num - 1) not in numSet:
                length = 1 # now we know its 1 not 0
                while (num + length) in numSet:
                    length += 1
                res = max(res, length)
        
        return res