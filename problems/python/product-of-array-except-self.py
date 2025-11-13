# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # nums = [1,2,3,4] 
        # left2right = [1, 1, 1*2=2, 2*3=6]
        # right2left = [2*12=24, 3*4=12, 4, 1]
        # output: for nums[i], res[i] = left2right[i] * right2left[i]

        n = len(nums)
        left2right = [1] * n
        right2left = [1] * n

        for i in range(1, n):
            left2right[i] = left2right[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            right2left[i] = right2left[i+1] * nums[i+1]

        res = []
        for i in range(n):
            res.append(left2right[i] * right2left[i])
        return res