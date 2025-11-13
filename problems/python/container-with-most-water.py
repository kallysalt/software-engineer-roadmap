# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:

        
        # height = [1,8,6,2,5,4,8,3,7]
        #           i               ] j
        # output: 49

        # solution 1: brute force - compute the area between any two lines
        # n + (n-1) + (n - 2) + ... + 2 + 1 = n^2

        # res = 0
        # n = len(height)

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         area = (j - i) * min(height[i], height[j]) 
        #         res = max(res, area)
            
        # return res
       
        # solution 2: 我不理解!
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r]) 
            res = max(res, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res
