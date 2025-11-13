# https://leetcode.com/problems/concatenation-of-array/description/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # create an array ans of length n where
        # ans[i] == nums[i]
        # ans[i + n] == nums[i]

        n = len(nums)
        res = [0] * 2 * n
        
        res[:n] = nums[:]
        res[n:] = nums[:]

        return res
        