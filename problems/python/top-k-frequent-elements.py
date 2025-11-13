# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent_1(self, nums: List[int], k: int) -> List[int]:

        # solution 1: brute force

        # count the occurance of each num, store in hmap
        # key: num, val: occurance
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        # sort 
        # we cannot sort the hmap
        # but we can convert the hamp to an array of tuples
        arr = []
        for num, cnt in hmap.items():
            arr.append((cnt, num))
        arr.sort() # sort the arry in place, small to large

        # return
        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res
        # time complexity = nlogn


    def topKFrequent_2(self, nums: List[int], k: int) -> List[int]:

        # solution 2: heapify all then pop k
        from collections import heapq
        
        # count the occurance of each num, store in hmap
        # key: num, val: occurance
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        # heapify 
        # we cannot heapify a hmap
        # but we can convert the hamp to an array of tuples
        minheap = []
        for num, cnt in hmap.items():
            minheap.append((-cnt, num))
        heapq.heapify(minheap) # heapq heapify the original list in place

        # return
        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res
        # time complexity = n + m + klog(m)
    
    
    def topKFrequent_3(self, nums: List[int], k: int) -> List[int]:

        # solution 3: keep a heap that stores the k most frequent items seen so far
        
                # count the occurance of each num, store in hmap: O(n)
        # key: num, val: occurance
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        # keep a heap that stores the k most frequent items seen so far
        minheap = []
        for num in hmap.keys():
            heapq.heappush(minheap, (hmap[num], num))
            if len(minheap) > k:
                heapq.heappop(minheap) # pop the smallest, keep the larger ones

        # return
        res = []
        while minheap:
            res.append(heapq.heappop(minheap)[1])
        return res

        # time complexity = n + m + klog(k) = n + m
    
    
        

        