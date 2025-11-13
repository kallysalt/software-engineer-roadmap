# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # edge cases: 
        # nums1 is empty arr, nums2 is empty arr

        # solution 1: first combine, then sort, time complexity = nlogn
        # nums1[m:] = nums2[:]
        # nums1.sort()

        # solution 2: create an arr to store original elements in nums1
        # need to fill ouy the rest when one ptr has reached end of arr
        # time complexity = n, need additional extra space

        nums1_copy = nums1[:m]
        i, j, k = 0, 0, 0

        while( i < m and j < n):
            if nums1_copy[i] <= nums2[j]:
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        
        if i < m:
            nums1[k:] = nums1_copy[i:]
        if j < n:
            nums1[k:] = nums2[j:]
