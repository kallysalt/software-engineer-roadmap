# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # already sorted -> two pointers
        # left pointer: start from 0 (first element)
        # right pointer: start from -1 (last element)
        # sum = numbers[l]+numbers[r]
        # if total < target: need to increase sum -> inc left by 1
        # if total > target: need to reduce sum -> dec right by 1
        # else: found it! 

        l,r = 0, len(numbers) - 1
        
        while l < r:
            total = numbers[l] + numbers[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return [l+1, r+1]