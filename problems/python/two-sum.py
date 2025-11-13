# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # use hashmap to store elements we've seen before
        # we want to check if given num exists
        # we also want to know original idx of the given num
        # key: num, val: idx

        hmap = {} 
        for idx, num in enumerate(nums):
            
            # check if hmap contains target - num
            # if yes: return [hmap[target-num], idx]
            # if no: store num and its idx in hmap

            if (target - num) in hmap:
                return [hmap[target-num], idx]
            else:
                hmap[num] = idx